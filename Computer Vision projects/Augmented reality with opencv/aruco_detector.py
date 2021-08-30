import numpy as np
import cv2

im_src = cv2.imread("Artificial-Intelligence/Computer Vision projects/Augmented reality with opencv/test.jpg")

cap  = cv2.VideoCapture(0)

outputFile = "ar_out_py.avi"
vid_writer = cv2.VideoWriter(outputFile, cv2.VideoWriter_fourcc('M','J','P','G'), 28, (round(2*cap.get(cv2.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

winName = "Augmented Reality using Aruco markers in OpenCV"

while True:
    # try:
        # get frames 
        ret, frame = cap.read()
        
        if not ret:
            print('end of file')
        
        # load the dictionary that was used to generate the markers
        ar_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        
        # initialize the detector parameters with default values
        parameters = cv2.aruco.DetectorParameters_create()
        
        # detect the markers in the image
        mc ,mIds,rejects = cv2.aruco.detectMarkers(frame,ar_dict, parameters = parameters)
        
        index = np.squeeze(np.where(mIds =33))
        refernce_pt1 = np.squeeze(mc[index[0]])[1]
        
        index = np.squeeze(np.where(mIds =34))
        refernce_pt2 = np.squeeze(mc[index[0]])[2]
        
        distance = np.linalg.norm(refernce_pt1-refernce_pt2)
        
        scale_factor =0.02
        pts_dist = [[refernce_pt1[0]- round(scale_factor*distance),refernce_pt1[1]-round(scale_factor*distance)]]
        pts_dist = pts_dist+[[refernce_pt2[0]- round(scale_factor*distance),refernce_pt2[1]-round(scale_factor*distance)]]
        
        index = np.squeeze(np.where(mIds =35))
        refernce_pt3 = np.squeeze(mc[index[0]])[0]
        pts_dist = pts_dist+[[refernce_pt3[0]- round(scale_factor*distance),refernce_pt3[1]-round(scale_factor*distance)]]
        
        index = np.squeeze(np.where(mIds =36))
        refernce_pt4 = np.squeeze(mc[index[0]])[0]
        
        # distance calculation between the different points
        pts_dist = pts_dist+[[refernce_pt4[0]- round(scale_factor*distance),refernce_pt4[1]-round(scale_factor*distance)]]
        
        # set the source points for the image to be portrayed
        pts_src =[[0,0],[im_src.shape[1],0],[im_src.shape[1],im_src.shape[0]],[0,im_src.shape[0]]]
        
        # set the source and distance as array format
        pts_src_m = np.asarray(pts_src)
        pts_dist_m = np.asarray(pts_dist)
        
        # calculate Homography
        h, status = cv2.findHomography(pts_src_m,pts_dist_m)
        
        # warp source image to the destinantion based on homography
        warped_image = cv2.warpPerspective(im_src,h,(frame.shape[1],frame.shape[0]))
        
        #  Prepare a mask representing the region to compy from the warped imahe into original frame
        mask = np.zeros([frame.shape[0],frame.shape[1]],dtype =np.uint8)
        cv2.fillConvexPoly(mask,np.int32([pts_dist_m]),(255, 255, 255), cv2.LINE_AA)
        
        # Erode the mask to not copy the boundry effects from the warping
        element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
        mask =cv2.erode(mask,element,iterations =3)
        
        # copy the mask into 3 channels
        warped_image = warped_image.astype(float)
        mask3 = np.zeros_like(warped_image)
        for i in range(0,3):
            mask3[:,:,i] =mask/255
        
        # copy the warped image into the original frame in the mask region
        warped_image_masked = cv2.multiply(warped_image,mask3)
        frame_masked = cv2.multiply(frame.astype(float),1-mask3)
        im_out = cv2.add(warped_image_masked,frame_masked)
        
        # showing the original image and the new output image side by side
        concat_out = cv2.concat([frame.astype(float),im_out])
        cv2.imshow("AR using Aruco markers", concat_out.astype(np.uint8))
        
        vid_writer.write(concat_out.astype(np.uint8))
        
        # break the loop if 'q' key pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # except Exception as e:
    #     print(e)    

cap.release()
cv2.destroyAllWindows()
if 'vid_writer' in locals():
    vid_writer.release()
    print('Video writer released..')       
        
        