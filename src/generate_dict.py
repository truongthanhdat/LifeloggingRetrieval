import os
import numpy as np
import pickle

from set import Set

# CAPTION

capt_set = Set()

captions = pickle.load(open(config.MERGE_CAPTION_PATH, 'rb'))
for caption in captions:
    words = caption.value()

# ENTITY

# PLACE

