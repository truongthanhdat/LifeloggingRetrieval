import cv2
import config
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt

VOTE = []

def calc_pixel_different(img1, img2):
    diff = img1[:, :, 0] - img2[:, :, 0]
    return np.abs(diff).astype(np.float) / 179.0

def compare(img1, img2, pix_thresh = config.PIXEL_THRESHOLD, vote_thresh = config.VOTE_THRESHOLD):
    if img1.shape != img2.shape:
        return False

    diff = calc_pixel_different(img1, img2).flatten()
    vote = float(len(diff[diff <= pix_thresh])) / float(len(diff))
    VOTE.append(vote)
    return True if vote >= vote_thresh else False

def load_image(image_name, image_dir=config.IMAGE_DIR):
    image_path = os.path.join(image_dir, image_name)
    image = cv2.imread(image_path)
    assert image is not None, 'Cannot load image from %s' % image_path
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return image

if __name__ == '__main__':
    shots = {}
    file_names = os.listdir(config.IMAGE_DIR)
    file_names.sort()

    current = file_names[0]
    shots[0] = [current]
    length = 1

    for i, file_name in enumerate(file_names[1:100]):
        img1 = load_image(current)
        img2 = load_image(file_name)
        if compare(img1, img2):
            shots[length - 1].append(file_name)
        else:
            shots[length] = [file_name]
            length = length + 1
        current = file_name
        per = float(i + 1) / len(file_names[1:]) * 100
        print 'Processing {0:.2f}%.'.format(per) , \
                'Finish process image %s. Number of current shots: %d' % (os.path.join(config.IMAGE_DIR, file_name), length)

    pickle.dump(shots, open(os.path.join(config.DATABASE_DIR, 'shots.pickle'), 'wb'))

    plt.plot(VOTE)
    plt.show()
