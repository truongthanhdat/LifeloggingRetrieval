import os
import numpy as np
import pickle
import config
import re
from sets import Set

# CAPTION

capt_set = Set()

captions = pickle.load(open(config.MERGE_CAPTION_PATH, 'rb'))
for caption in captions:
    words = Set(re.findall(r"[\w']+", captions[caption]))
    capt_set = capt_set | words

np.save(config.CAPTION_DICT_PATH, np.array(list(capt_set)))

# ENTITY

enti_set = Set()
entity_filenames = os.listdir(config.ENTITY_DIR)

for filename in entity_filenames:
    file_path = os.path.join(config.ENTITY_DIR, filename)
    ps = pickle.load(open(file_path, 'rb')).items()

    cur_set = Set()
    for p in ps:
        cur_set.add(p[1][0])

    enti_set = enti_set | cur_set

np.save(config.ENTITY_DICT_PATH, np.array(list(enti_set)))

# PLACE
place_set = Set()
place_filenames = os.listdir(config.PLACE_DIR)
for filename in place_filenames:
    file_path = os.path.join(config.PLACE_DIR, filename)
    a = np.load(file_path)

    cur_set = Set()
    for phrase in a[:10]:
        cur_set = cur_set | Set(re.split('_|/', phrase))

    place_set = place_set | cur_set

np.save(config.PLACE_DICT_PATH, np.array(list(place_set)))
