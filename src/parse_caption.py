import os
import json
import pickle
import config

file = {}
file_names = os.listdir(config.CAPTIONS_DIR)
for file_name in file_names:
    file[file_name] = json.load(open(os.path.join(config.CAPTIONS_DIR, file_name), 'r'))

img_names = [name.split('.')[0] for name in os.listdir(config.IMAGE_DIR)]

captions = {}
for img_name in img_names:
    cap = []
    for file_name in file_names:
        if file[file_name].has_key(img_name):
            cap.append(file[file_name][img_name])
    captions[img_name] = '$'.join(cap)

pickle.dump(captions, open(config.MERGE_CAPTION_PATH, 'wb'))

