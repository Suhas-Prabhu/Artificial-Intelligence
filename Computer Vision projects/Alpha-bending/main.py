import cv2

def aphablend(fore_img, back_img):
    # convert uint8 to float
    fore = fore_img.astype(float)
    back = back_img.astype(float)
    
    # normalize the alpha mask to keep the values between 0 and 1
    


img1 = cv2.imread('Artificial-Intelligence/Computer Vision projects/Alpha-bending/data/foreGroundAsset.png')
img2 = cv2.imread('Artificial-Intelligence/Computer Vision projects/Alpha-bending/data/back.jpg')