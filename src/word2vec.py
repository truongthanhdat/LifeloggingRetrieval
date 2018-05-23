from gensim.models import KeyedVectors
import config
from sklearn.neighbors import KDTree

def load_model(model_path=config.WORD2VEC_MODEL):
    word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)
    return word_vectors

def build_KDTree(vector):
    kdt = KDTree(vector, leaf_size=30, metric='euclidean')
    return kdt

if __name__ == '__main__':
    model = load_model()
    print model.keys()
