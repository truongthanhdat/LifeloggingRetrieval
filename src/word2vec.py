from gensim.models import KeyedVectors
import config
import pyflann
import time
import numpy as np
import os

def load_model(model_path=config.WORD2VEC_MODEL):
    print('Loading model ...')
    duration = time.time()
    word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True).wv
    duration = time.time() - duration
    print('Loading model takes %f second' % duration)
    return word_vectors

def build_KDTree(dictionary, model, data_path=config.DATA_KD_TREE_PATH):
    print('Building KD Tree...')
    duration = time.time()
    dictionary = [word for word in dictionary if word in model.vocab]
    if not os.path.exists(data_path):
        vectors = np.array([model[word] for word in dictionary], dtype=config.DTYPE_FLOAT)
        np.save(data_path, vectors)
    else:
        vectors = np.load(data_path)

    flann = pyflann.FLANN()
    flann.build_index(vectors)
    tree = {'kd_tree': flann, 'dictionary': dictionary}
    duration = time.time() - duration
    print('Building KD Tree takes %f second' % duration)
    return tree

def search(word, model, tree, top=config.TOP_WORD_RETRIEVAL, thresh=config.WORD_RETRIEVAL_THRESHOLD):
    duration = time.time()
    vector = model[word].reshape(1, -1).astype(config.DTYPE_FLOAT)
    index, dist = tree['kd_tree'].nn_index(vector, num_neighbors=top)
    answer = [tree['dictionary'][i] for i in index[0]]
    duration = time.time() - duration
    print('Searching takes %f second' % duration)
    return answer

if __name__ == '__main__':
    dictionary = np.load(config.DICTIONARY_PATH).tolist()
    model = load_model()
    tree = build_KDTree(dictionary, model)

    print search('salad', model, tree)

    tree['kd_tree'].delete_index()
    del tree

