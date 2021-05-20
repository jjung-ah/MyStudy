import cv2
import numpy as np
import matplotlib.pylab as plt

def drawing():
    img = np.zeros((512, 512, 3), np.uint8)
    
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    
    #font = cv2.FONT_HERSHET_SIMPLEX
    #cv2.putText(img, 'Hello', (10, 500), font, 4, (255, 255, 255), 2)
    
    plt.imshow(img)


drawing()