# This script is for downloading training image files from URL of image database http://image-net.org/

# Fix `urllib` functions:
# https://stackoverflow.com/questions/36516183/what-should-i-use-to-open-a-url-instead-of-urlopen-in-urllib3

from urllib import urlopen, urlretrieve
import cv2
import numpy as np
import os


def store_raw_images():
    # Sports and Atheltics image URLs:
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513

    # Download images from these 2 urls below to get ~20000 images
    # neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    # pic_num = 953
    neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    pic_num = 1
    neg_image_urls = urlopen(neg_images_link).read().decode()

    # Create directory for Negative images
    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            # Download image from each URL
            urlretrieve(i, "neg/" + str(pic_num) + ".jpg")

            # Convert image to greyscale
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)

            # Resize image width and height
            #  should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))

            # Save resized image
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)

            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    """
    Handling error images that has been downloaded

    :return:
    """
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly, question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


# store_raw_images()
# find_uglies()
create_pos_n_neg()
