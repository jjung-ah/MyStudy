from PIL import Image
from matplotlib.patches import Polygon, Rectangle
from matplotlib import pyplot as plt
import numpy as np
import os
from glob import glob


# jpg파일에 맞는 txt파일의 좌표를 나타내주는 annotation이미비를 출력해주는 함수

def VisualizeImage(imFile):
    AnnotationFile = imFile.split(".jpg")[0] + ".txt"
    if os.path.isfile(AnnotationFile):
        try:
            print(imFile)
            with open(AnnotationFile, "r", encoding='utf-8') as of:
                lblLines = of.readlines()
            print(lblLines)
            for i in range(len(lblLines)):
                labelLine = lblLines[i].split(' ')
                coords = list(map(lambda f: float(f), labelLine[1:]))
                x_center, y_center, bbox_w, bbox_h = coords[0], coords[1], coords[2], coords[3]
                #print(x_center, y_center, bbox_w, bbox_h)

                img = Image.open(imFile)
                w, h = img.size
                #print(w, h)

                rex_x, rec_y, rec_w, rec_h = (x_center - bbox_w/2)*w, (y_center - bbox_h/2)*h, bbox_w*w, bbox_h*h

                Korim = np.array(img, dtype=np.uint8)
                #plt.figure(figsize=(24, 12))    
                ax1 = plt.subplot(111)

                # Display the image
                #ax1.imshow(Korim)
                newPt = [[rex_x, rec_y], [rex_x+rec_w, rec_y], [rex_x+rec_w, rec_y+rec_h], [rex_x, rec_y+rec_h]]
                rect = Polygon(newPt, linewidth=2.5, edgecolor='g', facecolor='none')
                ax1.add_patch(rect)
            plt.figure(figsize=(24, 12))    
            ax1.imshow(Korim)
            plt.show()
        except:
            pass






# 실행 코드
DataPath2 = 'E:\\original_data\\kfood(21.5.6)_N2A\\완료\\라볶이\\'

img_list = glob(DataPath2 + '*.jpg')
for imFile in img_list:
    VisualizeImage2(imFile)