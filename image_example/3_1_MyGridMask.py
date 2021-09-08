import matplotlib.pyplot as plt
import matplotlib.image as img

def gridMask(path, w_num, h_num):
    #image = img.imread('E:\\Python_Project\\food10\\images\\1\\1.jpg')
		image = img.imread(path)
		h, w, c = image.shape
		#w_num, h_num = 9, 7  # 내가 그리고 싶은 네모 박스의 갯수 (w, h)
		w_n = int(w/(w_num*2+1))
		h_n = int(h/(h_num*2+1))
		#print(n1, n2, w_n, h_n)
		
		for i in range(w_num):
		    for j in range(h_num):
		        cv2.rectangle(image, (w_n*(2*i+1),h_n*(2*j+1)), (w_n*(2*i+2),h_n*(2*j+2)), (0,0,0), -1)
		
		plt.imshow(image)
		plt.show()
		
		return image