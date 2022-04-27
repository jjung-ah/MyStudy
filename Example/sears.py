# sears.py
bill_thickness = 0.11 * 0.001 # 지폐의 두께(0.11 mm)를 미터로 환산
sears_height = 442 # 높이(미터)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)


############################################################3



import os
import cv2
from omegaconf import DictConfig
import pathlib
from collections import defaultdict
from glob import glob
import shutil
from tqdm import tqdm
from pathlib import Path
import random


IMAGE_EXTENSION = ['.jpg', '.jpeg', '.png']

def is_image(paths: list):
    images = []
    for item in paths:
        name, ext = os.path.splitext(item)
        if ext in IMAGE_EXTENSION:
            images.append(item)
    return images


class Pipeline:
    def __init__(self, cfg: DictConfig):
        self.cfg = cfg

    def make_folder(self, path: str):
        if not os.path.isdir(path):
            os.makedirs(path)
        return path

    def get_subfolder(self, dirname: str):
        subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
        for dirname in list(subfolders):
            subfolders.extend(self.get_subfolder(dirname))
        return subfolders

    def get_path_subfolders(self, root_dir):  # dataset pairwise 및 split에 사용
        # sub_folders = ['Right', 'Rotation', 'Top', 'Top1', 'Front', 'Front_6']
        path_dirs_list = []
        for (path, dirs, files) in os.walk(root_dir):
            if set(dirs) - set(self.cfg.datasets.sub_folders) == set() and dirs != []:
                path_dirs_list.append([path, dirs])
        return path_dirs_list

    def check_datasets_file(self, root_dir: str):
        run_dataset = self.cfg.datasets.run_dataset
        for i in run_dataset:
            file_path = os.path.join(root_dir, self.cfg.datasets.check_dir.last_dataset, i + '.txt')
            if os.path.isfile(file_path):
                return True
            else:
                return False

    def check_dataset_folder(self, image_folder_dict: dict):
        folder_path_list = []
        # raw_sub = self.get_path_subfolders(list(image_folder_dict.keys())[0])
        raw_sub = self.get_path_subfolders(self.cfg.datasets.root_dir.path)
        inspected_sub = self.get_path_subfolders(self.cfg.datasets.output_inspected_dir)
        raw_sub_list = [i[0].split(f'{os.sep}')[-2:] for i in raw_sub]
        inspected_sub_list = [i[0].split(f'{os.sep}')[-2:] for i in inspected_sub]
        intersection_folder = [i for i in raw_sub_list if i in inspected_sub_list]
        new_dataset_folder = [i for i in raw_sub_list if i not in inspected_sub_list]
        return [new_dataset_folder, image_folder_dict], [intersection_folder, image_folder_dict]

    def make_image_list(self, root_dir: str):
        image_list = []
        subfolders = self.get_subfolder(root_dir)
        # subfolders = self.get_select_folder(root_dir)
        sub = [os.path.dirname(i) for i in subfolders if i.find('image') != -1]
        for path in sub:
            dir_path = os.path.join(path, 'image')
            image_list += glob(dir_path + f'{os.sep}' + '*')
            image_list = is_image(image_list)
        return image_list

    def make_mask_list(self, root_dir: str):
        mask_list = []
        subfolders = self.get_subfolder(root_dir)
        # subfolders = self.get_select_folder(root_dir)
        sub = [os.path.dirname(i) for i in subfolders if i.find('mask') != -1]
        for path in sub:
            dir_path = os.path.join(path, 'mask')
            mask_list += glob(dir_path + f'{os.sep}' + '*')
            mask_list = is_image(mask_list)
        return mask_list

    def make_image_pairwise(self, image_list: str):
        image_pair_dict = dict()
        for f in image_list:
            file_base_name = os.path.basename(f).split('_')[0]
            if image_pair_dict.get(file_base_name) == None:
                image_pair_dict[file_base_name] = [f]
            else:
                image_pair_dict[file_base_name].append(f)
        return image_pair_dict

    def make_image_mask_pairwise(self, image_list: str):
        image_mask_pair_dict = dict()
        for f in image_list:
            file_base_name = os.path.basename(f).split('_')[0]
            view_name = os.path.dirname(f).split(os.sep)[-2]
            if image_mask_pair_dict.get((file_base_name, view_name)) == None:
                image_mask_pair_dict[(file_base_name, view_name)] = [f]
            else:
                image_mask_pair_dict[(file_base_name, view_name)].append(f)
        return image_mask_pair_dict

    def check_split_num(self, image_pair_dict: dict):
        length = len(list(image_pair_dict.keys()))
        return length

    def make_path_list(self, key_name_set: list, path_dict: dict):  # dict to list
        path_list = []
        for i in key_name_set:
            path_list += path_dict[i]
        return path_list

    def split_shuffle_test_list(self, image_pair_dict: dict):
        test_keys, test_list = [], []
        train_val_dict = dict()
        pair_keys = list(image_pair_dict.keys())
        print(len(pair_keys))
        if len(pair_keys) >= self.cfg.datasets.num:
            train_val_keys = random.sample(pair_keys, self.cfg.datasets.num)  # 이걸로 해야하나.. 아니면 shuffle 후에 100개를 잘라야하나..?
        else:
            train_val_keys = random.sample(pair_keys, len(pair_keys))
        test_keys += list(set(pair_keys) - set(train_val_keys))
        for i in train_val_keys:
            train_val_dict[i] = image_pair_dict[i]
        test_list = self.make_path_list(test_keys, image_pair_dict)
        return train_val_dict, test_list

    def split_train_val_dict(self, train_val_dict, max=True, sample_num=50):
        file_key = list(train_val_dict.keys())
        if self.cfg.datasets.shuffle == True:
            random.shuffle(file_key)
        if max == True:
            length = len(train_val_dict)
        else:
            length = sample_num
        split_num = int(length * self.cfg.datasets.ratio)
        train_set = file_key[:split_num]
        val_set = file_key[split_num:]
        train_datasets = self.make_path_list(train_set, train_val_dict)
        val_datasets = self.make_path_list(val_set, train_val_dict)
        return train_datasets, val_datasets

    def make_run_dataset_list(self, inspected_dir):  # from inspected to text
        run_dataset_dict = dict()
        run_dataset = self.cfg.datasets.run_dataset
        for i in run_dataset:
            dir_path = os.path.join(inspected_dir, i)
            image_list = self.make_image_list(dir_path)
            run_dataset_dict[i] = image_list
        return run_dataset_dict


    #####################################################################################################
    def make_train_val_test(self, root_dir, num):
        train_val_test_dict = dict()
        image_list = self.make_image_list(root_dir)
        image_pair_dict = self.make_image_pairwise(image_list)
        train_val_dict, test_datasets = self.split_shuffle_test_list(image_pair_dict)
        train_datasets, val_datasets = self.split_train_val_dict(train_val_dict, True, num)
        train_val_test_dict = {'train': train_datasets, 'val': val_datasets, 'test': test_datasets}
        return train_val_test_dict

    def add_train_val_test(self, new_dataset_folder, sample_num):
        image_list = list(new_dataset_folder.values())[0]
        image_pair_dict = self.make_image_pairwise(image_list)
        train_val_dict, test_datasets = self.split_shuffle_test_list(image_pair_dict)
        train_datasets, val_datasets = self.split_train_val_dict(train_val_dict, True, sample_num)
        train_val_test_dict = {'train': train_datasets, 'val': val_datasets, 'test': test_datasets}
        return train_val_test_dict

    def add_train_val(self, intersection_folder, sample_num):
        image_list = list(intersection_folder.values())[0]
        print(image_list)
        image_pair_dict = self.make_image_pairwise(image_list)
        print(image_pair_dict)
        train_datasets, val_datasets = self.split_train_val_dict(image_pair_dict, False, sample_num)
        train_val_dict = {'train': train_datasets, 'val': val_datasets}
        return train_val_dict

    ########################################################################################################
    def is_label(self):
        pass

    # def save_image_datasets(self, image_dict):
    #     # self.make_folder(os.path.dirname(out_dir))
    #     image_api = Images()
    #     run_dataset = list(image_dict.keys())
    #     for i in run_dataset:
    #         for image in tqdm(image_dict[i]):
    #             # save image
    #             out_path, file_name = os.path.split(image)[0], os.path.split(image)[1]
    #             out_path = out_path.replace(self.cfg.datasets.root_dir.path, os.path.join(self.cfg.datasets.output_inspected_dir, i))
    #             self.make_folder(out_path)
    #             image_api.copy_image(image, os.path.join(out_path, file_name))
    #             # save mask
    #             mask_path = image.replace('image', 'mask')
    #             mask_out_path = out_path.replace('image', 'mask')
    #             self.make_folder(mask_out_path)
    #             image_api.copy_image(mask_path, os.path.join(mask_out_path, file_name))

    def save_image_datasets(self, image_dict):
        # self.make_folder(os.path.dirname(out_dir))
        image_api = Images()
        run_dataset = list(image_dict.keys())
        for i in run_dataset:

            # image_list = image_dict[i]
            # dir_name = [os.path.dirname(i) for i in image_list]
            # dir_name = list(set(dir_name))
            # mask_list = []
            # for d in dir_name:
            #     mask_list += glob(os.path.join(d.replace('image', 'mask'), '*'))
            # all_list = image_list + mask_list
            # image_mask_pair_dict = self.make_image_mask_pairwise(all_list)

            # for image in tqdm(image_dict[i]):
            image_list = image_dict[i]
            dir_name = [os.path.dirname(i) for i in image_list]
            dir_name = list(set(dir_name))
            mask_list = []
            for d in dir_name:
                mask_list += glob(os.path.join(d.replace('image', 'mask'), '*'))
            all_list = image_list + mask_list
            image_mask_pair_dict = self.make_image_mask_pairwise(all_list)

            for key in list(image_mask_pair_dict.keys()):
                # if len(image_mask_pair_dict[key]) == 1:
                #     image = image_mask_pair_dict[key][0]
                #     out_path, file_name = os.path.split(image)[0], os.path.split(image)[1]
                #     out_path = out_path.replace(self.cfg.datasets.root_dir.path,
                #                                 os.path.join(self.cfg.datasets.output_inspected_dir, i))
                #     self.make_folder(out_path)
                #     image_api.copy_image(image, os.path.join(out_path, file_name))
                if len(image_mask_pair_dict[key]) == 2:
                    image = image_mask_pair_dict[key][0]
                    out_path, file_name = os.path.split(image)[0], os.path.split(image)[1]
                    out_path = out_path.replace(self.cfg.datasets.root_dir.path,
                                                os.path.join(self.cfg.datasets.output_inspected_dir, i))
                    self.make_folder(out_path)
                    image_api.copy_image(image, os.path.join(out_path, file_name))
                    mask = image_mask_pair_dict[key][1]
                    mask_path, mask_file_name = os.path.split(mask)[0], os.path.split(mask)[1]
                    mask_out_path = mask_path.replace(self.cfg.datasets.root_dir.path, os.path.join(self.cfg.datasets.output_inspected_dir, i))
                    self.make_folder(mask_out_path)
                    image_api.copy_image(mask, os.path.join(mask_out_path, mask_file_name))

    def save_text(self, image_dict: dict, out_dir: str):
        for i in self.cfg.datasets.run_dataset:
            out_path = os.path.join(out_dir, '{}.txt'.format(i))
            self.make_folder(os.path.dirname(out_path))
            if self.is_label() == False:
                with open(out_path, 'a', encoding="UTF-8") as f:
                    for i in tqdm(image_dict[i]):
                        image = i
                        mask = image.replace('image', 'mask')
                        data = image + '\t' + mask + '\n'
                        f.write(data)
            else:
                with open(out_path, 'a', encoding="UTF-8") as f:
                    for i in tqdm(image_dict[i]):
                        image = i
                        mask = image.replace('image', 'mask')
                        data = image + '\t' + mask + '\n'
                        f.write(data)

    # def save_text(self, image_dict: dict, out_dir: str):
    #     for i in self.cfg.datasets.run_dataset:
    #         out_path = os.path.join(out_dir, '{}.txt'.format(i))
    #         self.make_folder(os.path.dirname(out_path))
    #         if self.is_label() == False:
    #             with open(out_path, 'a', encoding="UTF-8") as f:
    #                 image_list = image_dict[i]
    #                 dir_name = [os.path.dirname(i) for i in image_list]
    #                 dir_name = list(set(dir_name))
    #                 mask_list = []
    #                 for d in dir_name:
    #                     mask_list += glob(os.path.join(d.replace('image', 'mask'), '*'))
    #                 all_list = image_list + mask_list
    #                 image_mask_pair_dict = self.make_image_mask_pairwise(all_list)
    #                 for key in tqdm(list(image_mask_pair_dict.keys())):
    #                     if len(image_mask_pair_dict[key]) == 1:
    #                         data = image_mask_pair_dict[key][0] + '\n'
    #                         f.write(data)
    #                     elif len(image_mask_pair_dict[key]) == 2:
    #                         data = image_mask_pair_dict[key][0] + '\t' + image_mask_pair_dict[key][1] + '\n'
    #                         f.write(data)
    #         else:
    #             with open(out_path, 'a', encoding="UTF-8") as f:
    #                 image_list = image_dict[i]
    #                 dir_name = [os.path.dirname(i) for i in image_list]
    #                 dir_name = list(set(dir_name))
    #                 mask_list = []
    #                 for d in dir_name:
    #                     mask_list += glob(os.path.join(d.replace('image', 'mask'), '*'))
    #                 all_list = image_list + mask_list
    #                 image_mask_pair_dict = self.make_image_mask_pairwise(all_list)
    #                 for key in tqdm(list(image_mask_pair_dict.keys())):
    #                     if len(image_mask_pair_dict[key]) == 1:
    #                         data = image_mask_pair_dict[key][0] + '\n'
    #                         f.write(data)
    #                     elif len(image_mask_pair_dict[key]) == 2:
    #                         data = image_mask_pair_dict[key][0] + '\t' + image_mask_pair_dict[key][1] + '\n'
    #                         f.write(data)

    def copy_text(self, check_dir, output_run_dir):
        if not os.path.exists(output_run_dir):
            shutil.copytree(check_dir, output_run_dir)

    def make_new_dataset_folder(self, new_dataset_folder):
        train_val_test_dict = self.add_train_val_test(new_dataset_folder[1], self.cfg.datasets.sample_num)
        self.save_image_datasets(train_val_test_dict)
        run_dataset_dict = self.make_run_dataset_list(self.cfg.datasets.output_inspected_dir)
        self.save_text(run_dataset_dict, self.cfg.datasets.output_run_dir)

    def check_mask_dataset(self, intersection_folder):
        intersection_dict = dict()
        image_list = list(intersection_folder.values())[0]
        mask_list = self.make_mask_list(intersection_folder[1])
        image_name_list = [os.path.basename(file) for file in image_list]
        mask_name_list = [os.path.basename(file) for file in mask_list]
        test_name_list = list(set(image_name_list) - set(mask_name_list))
        train_val_name_list = list(set(image_name_list) - set(test_name_list))
        train_val_list = [os.path.join(os.path.split(image_list[0])[0], i) for i in train_val_name_list]
        intersection_dict[intersection_folder.keys()] = train_val_list
        test_list = [os.path.join(os.path.split(image_list[0])[0], i) for i in test_name_list]
        if test_list == []:
            pass
        else:
            image_api = Images()
            out_text_path = os.path.join(self.cfg.datasets.output_run_dir, 'text.txt')
            with open(out_text_path, 'a', encoding="UTF-8") as f:
                for file in test_list:
                    file_name = os.path.basename(file)
                    image_api.copy_image(file, os.path.join(self.cfg.datasets.output_run_dir, 'test', file_name))
                    image = file
                    mask = image.replace('image', 'mask')
                    data = image + '\t' + mask + '\n'
                    f.write(data)
        return intersection_dict

    def make_intersection_folder(self, intersection_folder):
        print(intersection_folder[1])
        intersection_dict = self.check_mask_dataset(intersection_folder)
        #train_val_dict = self.add_train_val(intersection_folder[1], self.cfg.datasets.sample_num)
        train_val_dict = self.add_train_val(intersection_dict, self.cfg.datasets.sample_num)
        self.save_image_datasets(train_val_dict)
        run_dataset_dict = self.make_run_dataset_list(self.cfg.datasets.output_inspected_dir)
        self.save_text(run_dataset_dict, self.cfg.datasets.output_run_dir)

    def make_run_datasets(self, path, run, image_dict):
        if run == 'add':
            # self.copy_text(os.path.join(self.cfg.datasets.check_dir.root_dir, self.cfg.datasets.check_dir.last_dataset), self.cfg.datasets.output_run_dir)
            new_dataset_folder, intersection_folder = self.check_dataset_folder(image_dict)
            if new_dataset_folder[0] != []:
                self.make_new_dataset_folder(new_dataset_folder)
            elif intersection_folder[0] != []:
                self.make_intersection_folder(intersection_folder)
            if new_dataset_folder[0] == [] and intersection_folder[0] == []:
                pass
        elif run == 'first':
            train_val_test_dict = self.make_train_val_test(path, self.cfg.datasets.num)
            self.make_folder(self.cfg.datasets.output_run_dir)
            self.save_image_datasets(train_val_test_dict)
            run_dataset_dict = self.make_run_dataset_list(self.cfg.datasets.output_inspected_dir)
            self.save_text(run_dataset_dict, self.cfg.datasets.output_run_dir)

    def make_run_folder(self):
        folders = []
        run_folder = self.cfg.datasets.root_dir.folder
        if run_folder == []:
            folders = self.get_path_subfolders(self.cfg.datasets.root_dir.path)
        else:
            for f in run_folder:
                path_dir = os.path.join(self.cfg.datasets.root_dir.path, f)
                subfolders = self.get_path_subfolders(path_dir)
                folders.extend(subfolders)
        return folders

    def add_run_datasets(self, run, folders):
        for j in folders:
            # self.make_run_datasets(j[0], run, image_folder_dict)
            diff_image_list = []
            image_folder_dict = dict()
            raw_image_list = self.make_image_list(j[0])
            inspected_image_list = self.make_image_list(self.cfg.datasets.output_inspected_dir)
            raw_image_name_list = [os.path.basename(file) for file in raw_image_list]
            inspected_image_name_list = [os.path.basename(file) for file in inspected_image_list]
            image_list = list(set(raw_image_name_list) - set(inspected_image_name_list))
            # print(image_list)
            for i in raw_image_list:
                if os.path.basename(i) in image_list:
                    diff_image_list.append(i)
            # print(diff_image_list)
            image_folder_dict[j[0]] = diff_image_list
            # print(image_folder_dict)
            self.make_run_datasets(j[0], run, image_folder_dict)

    def run(self):
        folders = self.make_run_folder()
        if self.check_datasets_file(self.cfg.datasets.check_dir.root_dir) == True:
            run = 'add'
            self.add_run_datasets(run, folders)
        else:
            run = 'first'
            for j in folders:
                # self.make_run_datasets(j[0], run, image_folder_dict)
                image_folder_dict = dict()
                raw_image_list = self.make_image_list(j[0])
                image_folder_dict[j[0]] = raw_image_list
                self.make_run_datasets(j[0], run, image_folder_dict)
    ############################################################################################################################


class Images:
    def __init__(self):
        pass

    def load_image(self, path):
        image = cv2.imread(path)
        if type == 'RGB':
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif type == 'L':
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image

    def save_image(self, path, image):
        cv2.imwrite(path, image)

    def copy_image(self, source, target):
        shutil.copy(source, target)

    def move_image(self, source, target):
        shutil.move(source, target)
