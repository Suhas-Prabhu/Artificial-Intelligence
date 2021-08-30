What is alpha blending?
Alpha blending is the process of overlaying a foreground image with transparency over a background image. The transparency is often the fourth channel of an image ( e.g. in a transparent PNG), but it can also be a separate image. This transparency mask is often called the alpha mask or the alpha matte.

In the feature image on the top of this article, the foreground image is shown on the top left, the gray scale alpha mask is shown on the top right, the background image is shown on the bottom left, and the composite image obtained by blending the foreground image and the background image using an alpha mask is shown in the bottom right.

The math behind alpha blending is straight forward. At every pixel of the image, we need to combine the foreground image color (F) and the background image color (B) using the alpha mask (\alpha).


Learn to build exciting Computer Vision applications with OpenCV and start your AI journey!
OpenCV For Beginners available at a discounted launch price of $87 (Standard Retail Price: $117).
Learn More
Note: The value of \alpha used in the equation is actually the pixel value in the alpha mask divided by 255. So, in the equation below, 0 \leq \alpha \leq 1
I = \alpha F + (1 - \alpha) B
From the equation above, you can make the following observations.

When \alpha = 0, the output pixel color is the background.
When \alpha = 1, the output pixel color is simply the foreground.
When 0 < \alpha < 1 the output pixel color is a mix of the background and the foreground. For realistic blending, the boundary of the alpha mask usually has pixels that are between 0 and 1.
