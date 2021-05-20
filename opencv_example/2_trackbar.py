import numpy as np
import cv2
import matplotlib.pyplot as plt

def onChange(x):
    pass

#def trackbar(img_name):
        #path = 'E:\\Python_Project\\yolov5\\multi\\original\\' + str(img_name) + '.jpg'
    #img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    
def trackbar():
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('color_palette')
    
    cv2.createTrackbar('B', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('G', 'color_palette', 0, 255, onChange)
    cv2.createTrackbar('R', 'color_palette', 0, 255, onChange)
    
    switch = '0: OFF\n1: ON'
    cv2.createTrackbar(switch, 'color_palette', 0, 1, onChange)
    
    while True:
        cv2.imshow('color_palette', img)
        k = cv2.waitKey(1) & 0xFF
        
        if k == 27:
            break
        
        b = cv2.getTrackbarPos('B', 'color_palette')
        g = cv2.getTrackbarPos('G', 'color_palette')
        r = cv2.getTrackbarPos('R', 'color_palette')
        s = cv2.getTrackbarPos(switch, 'color_palette')
        
        if s == 0:
            img[ : ] = 0
        else:
            img[ : ] = [b, g, r]
    
    cv2.destroyAllWindows()



trackbar()