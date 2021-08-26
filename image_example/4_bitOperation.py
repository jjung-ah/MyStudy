import numpy as np
import cv2

def bitOperation(hpos, vpos):
    img1 = cv2.imread('images/image1.jpg')
    img2 = cv2.imread('images/image2.jpg')

    # 로고를 1번 사진 왼쪽 윗부분에 두기 위해 해당 영역 지정하기
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    # 로고를 위한 마스크와 역마스크 생성하기
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # ROI에서 로고에 해당하는 부분만 검정색으로 만들기
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # 로고 이미지에서 로고 부분만 추출하기
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # 로고 이미지 배경을 cv2.add로 투명으로 만들고 ROI에 로고 이미지 넣기
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(10, 10)