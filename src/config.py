import numpy as np

# COMMON CONFIG

DTYPE_FLOAT = np.float32

#PATH CONFIG

IMAGE_DIR = '../Database/Images'
PLACE_DIR = '../Database/Place'
ATTRIBUTE_DIR = '../Database/Attributes'
ENTITY_DIR = '../Database/Entities'


#DATABASE

DATABASE_DIR = '/Users/truongthanhdat/Dataset/LSC/Database'

#IMAGE DISTACE THRESHOLD

PIXEL_THRESHOLD = 0.2
VOTE_THRESHOLD = 0.5

# WORD2VEC MODEL
WORD2VEC_MODEL = '../Database/GoogleNews-vectors-negative300.bin'
TOP_WORD_RETRIEVAL = 10
WORD_RETRIEVAL_THRESHOLD = 0.5
DICTIONARY_PATH = '../Database/dictionary.npy'

# KD-Tree
KD_TREE_INDEX_PATH = '../Database/kd_tree_index.flann'
DATA_KD_TREE_PATH = '../Database/kd_tree_data.npy'

# CAPTIONS
CAPTIONS_DIR = '../Database/Captions'
MERGE_CAPTION_PATH = '../Database/merge_caption.pickle'
