# PortSet
**PortSet** is a dataset for focusing on foreground objects in an image (like Portrait mode in phones!). This dataset is created so that you can train models which can detect background objects, foreground objects or even learn to directly blur the unimportant stuff in an image!

## Dataset
The dataset contains xxx images. 756 of them are realworld images (marked with `real_world`) and zzz of them are synthesized images (marked with `synthesized`). The synthesized images are created using _blender v3.0_ and different 3D objects and rendering conditions. More on the synthesis process can be found in the [synthesis](#synthesis) section.

The dataset consists of different imaging conditions and different camera positions, for sake of generalization. Also the pictures contain **indoor** and **outdoor** scenes. For example, you can see a set of input_image + blurred_image in 2 different conditions, below:

![input_image]("https://github.com/amirhossein-razlighi/PortSet/blob/main/readme_images/0_orig.jpg")
