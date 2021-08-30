ArUco stands for Augmented Reality University of Cordoba. That is where it was developed in Spain.An aruco marker is a fiducial marker that is placed on the object or scene being imaged. It is a binary square with black background and boundaries and a white generated pattern within it that uniquely identifies it. The black boundary helps making their detection easier. They can be generated in a variety of sizes. The size is chosen based on the object size and the scene, for a successful detection. If very small markers are not being detected, just increasing their size can make their detection easier.

Augmented Reality using ArUco Markers in OpenCV (C++ / Python)
Sunita Nayak
MARCH 21, 2020 LEAVE A COMMENT
Application Camera Calibration Computer Vision Stories how-to Tools Tutorial

In this post, we will explain what ArUco markers are and how to use them for simple augmented reality tasks using OpenCV.

ArUco markers have been used for a while in augmented reality, camera pose estimation, and camera calibration. Let’s learn more about them.

What are ArUco markers?
ArUco markers were originally developed in 2014 by S.Garrido-Jurado et al., in their work “Automatic generation and detection of highly reliable fiducial markers under occlusion“. ArUco stands for Augmented Reality University of Cordoba. That is where it was developed in Spain. Below are some examples of the ArUco markers.

Examples of aruco markers
An aruco marker is a fiducial marker that is placed on the object or scene being imaged. It is a binary square with black background and boundaries and a white generated pattern within it that uniquely identifies it. The black boundary helps making their detection easier. They can be generated in a variety of sizes. The size is chosen based on the object size and the scene, for a successful detection. If very small markers are not being detected, just increasing their size can make their detection easier.

The idea is that you print these markers and put them in the real world. You can photograph the real world and detect these markers uniquely.

If you are a beginner, you may be thinking how is this useful? Let’s look at a couple of use cases.

In the example we have shared in the post, we have put the printed and put the markers on the corners of a picture frame. When we uniquely identify the markers, we are able to replace the picture frame with an arbitrary video or image. The new picture has the correct perspective distortion when we move the camera.

In a robotics application, you can put these markers along the path of the warehouse robot equipped with a camera. When the camera mounted on the robot detects one these markers, it can know its precise location in the warehouse because each marker has a unique ID and we know where the markers were placed in the warehouse.

Generating ArUco markers in OpenCV
We can generate these markers very easily using OpenCV. The aruco module in OpenCV has a total of 25 predefined dictionaries of markers. All the markers in a dictionary contain the same number of blocks or bits(4×4, 5×5, 6×6 or 7×7), and each dictionary contains a fixed number of markers(50, 100, 250 or 1000). Below we show how to generate and detect various kinds of aruco markers in both C++ and Python.
The function call getPredefinedDictionary below shows how to load a dictionary of 250 markers, where each marker contains a 6×6 bit binary pattern.

Detecting Aruco markers
Once the scene is imaged with the aruco markers, we need to detect them and use them for further processing.

For each successful marker detection, the four corner points of the marker are detected, in order from top left, top right, bottom right and bottom left. In C++, these 4 detected corner points are stored as a vector of points and multiple markers in the image are together stored in a vector of vector of points. In Python, they are stored as Numpy array of arrays.

The detectMarkers function is used to detect and locate the corners of the markers. The first parameter is the image of the scene with the markers. The second parameter is the dictionary used to generate the markers. The successfully detected markers will be stored in markerCorners and their ids are stored in markerIds. The DetectorParameters object initialized earlier is also passed as a parameter. Finally, the rejected candidates are stored in rejectedCandidates.

While printing, cutting and placing the markers in a scene, it is important that we retain some white border around the marker’s black boundary, so that they can be detected easily.

For each image, the markers are first detected. The picture below shows the detected markers drawn in the green. The first point is marked with a small red circle. The second, third and fourth points can be accessed by traversing the border of the marker clockwise.

Four corresponding set of points in the input image and the new scene image are used to compute a homography. We explained homography in one of our earlier posts here. Given corresponding points in different views of a scene, homography is a transform that maps one corresponding point to another.

the homography matrix is used to warp the new scene image into the quadrilateral defined by the markers in our captured image.
We use the new scene image corner points as the source points(pts_src), and corresponding picture corner points inside the picture frame in our captured image as the destination points(dst_src). The OpenCV function findHomography computes the homography function h between the source and destination points. The homography matrix is then used to warp the new image to fit into the target frame. The warped image is masked and copied into the target frame. In case of video, this process is repeated on each frame.