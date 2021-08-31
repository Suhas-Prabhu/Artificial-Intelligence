# Alpha blending

## setup

*unfinished*

***

## How  it works
The process of  overlaying a foreground image with transperancy over a background image is called alpha blending. The transparency is often the fourth channel of an image. This transparency mask is often called the alpha mask or the alpha matte.


The math behind alpha blending is as follows,
At every pixel of the image, we need to combine the foreground image color (F) and the background image color (B) using the alpha mask (\alpha).



Note: The value of alpha used in the equation is actually the pixel value in the alpha mask divided by 255. So, in the equation below, 

0 &le; &alpha; &le;  1  

I = (&Alpha; * F) + (1 - &alpha;)* B

From the equation above, you can make the following observations.

When &alpha; = 0, the output pixel color is the background.

When &alpha; = 1, the output pixel color is simply the foreground.

When **0 &lt; &alpha; &lt; 1** the output pixel color is a mix of the background and the foreground. For realistic blending, the boundary of the alpha mask usually has pixels that are between 0 and 1.
