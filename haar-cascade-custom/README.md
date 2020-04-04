# Building Custom Haar Cascade

## Overview
To build a Haar Cascade, we need positive and negative images:

* Positive images: contains object we want to find. We can have only 1 of this positive image
* Negative images: random images excluding positive image. We need few thousands images for negative images

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
    opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
    ```
    The result should produce file `info.lst` with contents:
    ```
    0001_0014_0045_0028_0028.jpg 1 14 45 28 28
    ```
    filename + how many of your objects is in the image + all locations (x, y, width, height)
* Create positive image vector
    ```sh
    opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
    ```

## Train the cascade
* Create `data` directory into the workspace
* The new project structure will be like:
    ```
    opencv_workspace
    --neg
    ----negimages.jpg
    --opencv
    --info
    --data
    --positives.vec 
    --bg.txt
    --watch5050.jpg
    ```
* Run the training command on terminal:
    ```sh
    opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
    ```
    Note that we use significantly less `numPos` than we have. This is to make room for the stages, which will add to this.
    
    General concensus is, for most practices, you want to have `2:1` ratio of `pos:neg` images.
    
    Next, we have stages. We can use 10-20 stages. More stages means more longer training process will take.
    
    We can run the command overnight using this command:
    ```sh
    nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20 &
    ```
* Wait until file `cascade.xml` is produced in `data` directory.
* Download `cascade.xml` and put at the same directory as file [`haar-cascade-custom.py`](/haar-cascade-custom/haar-cascade-custom.py)
    * In the example at [`haar-cascade-custom.py`](/haar-cascade-custom/haar-cascade-custom.py), we renamed the cascade file to `watchcascade10stage.xml`


