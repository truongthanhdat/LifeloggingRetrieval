from gensim.models import KeyedVectors
import config
from sklearn.neighbors import KDTree

def load_model(model_path=config.WORD2VEC_MODEL):
    print('Load model ...')
    word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True).wv
    return word_vectors

def build_KDTree(vector):
    kdt = KDTree(vector, leaf_size=30, metric='euclidean')
    return kdt

if __name__ == '__main__':
    model = load_model()
    tree = build_KDTree(model)
    print(model.key())
