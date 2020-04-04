# Building Custom Haar Cascade

## Overview
To build a custom Haar Cascade, we need positive and negative images:

### Negative and Positive images
#### Negative images
* Random images excluding positive image. 
* We need few thousands images for negative images
* File `bg.txt` that contains path to each image line by line e.g: `neg/1.jpg`

#### Positive images
* Contains object we want to find. 
* We can have only 1 of this positive image and create the rest of these from negative images
* File `pos.txt` or `info` that contains path to each image line by line along with how many objects and where the objects located in the image e.g: `pos/1.jpg 1 0 0 50 50` (image, num_objects, x_position, y_position, rectangle_size)

### Notes
* Negative images quantity > Positive images quantity. If we create positive samples manually from negative samples
* Start by using small images:
  * 100x100 for Negatives
  * 50x50 for Positives
* Positive image should be doubled for training

## Steps to create custom Haar Cascade
1. Collect Negative or Background images
    * Any image will do, just make sure the object we want to find is not included. Get thousands.
2. Collect or Create Positive images
    * Thousands of image of the object we want to find. Can make these based on one image, or manually create them.
3. Create a positive vector file by stitching together all positives
    * We can create this using OpenCV command
4. Train cascade
    * We can run this using OpenCV command

## Create image vector
We create positive images from negative images

* Upload script [`download-image.py`](/haar-cascade-custom/download-image.py) to server
* Run function `create_pos_n_neg()` from [`download-image.py`](/haar-cascade-custom/download-image.py) to create `bg.txt`
* Project structure
    ```
    opencv_workspace
    --neg               --> Negative images
    ----negimages.jpg
    --opencv
    --info              --> Positive images
    --bg.txt
    --watch5050.jpg
    ``` 
* Create positive images based on `watch5050.jpg`. Run this command on terminal:
    ```sh
    $ cd haar-cascade-custom
    $ opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
    ```
    The result should produce file `info.lst` with contents:
    ```
    0001_0014_0045_0028_0028.jpg 1 14 45 28 28
    ```
    filename + how many of your objects is in the image + all locations (x, y, width, height)
* Create positive image vector
    ```sh
    $ opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
    ```

## Train the cascade
* Create `data` directory into the workspace
* The new project structure will be like:
    ```
    opencv_workspace
    --neg               --> Negative images
    ----negimages.jpg
    --opencv
    --info              --> Positive images
    ----posimages.jpg
    --data              --> Cascade files
    ----*.xml
    --positives.vec 
    --bg.txt
    --watch5050.jpg
    ```
* Run the training command on terminal:
    ```sh
    $ opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
    ```
    Note that we use significantly less `numPos` than we have. This is to make room for the stages, which will add to this.
    
    General consensus is, for most practices, you want to have `2:1` ratio of `pos:neg` images.
    
    Next, we have stages. We can use 10-20 stages. More stages means more longer training process will take.
    
    Above command takes ~4hours. We can run the command overnight using this command:
    ```sh
    $ nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &
    ```
    If above command interrupted, we can resume the process by running above command again. To see the progress we can run:
    ```sh
    $ tail -f nohup.out
    ```
  
* Wait until file `cascade.xml` is produced in `data` directory.
* Download `cascade.xml` and put at the same directory as file [`haar-cascade-custom.py`](/haar-cascade-custom/haar-cascade-custom.py)
    * In the example at [`haar-cascade-custom.py`](/haar-cascade-custom/haar-cascade-custom.py), we renamed the cascade file to `watchcascade10stage.xml`
    * Typical Haar Cascade file should be around `100-2,000KB` in size
