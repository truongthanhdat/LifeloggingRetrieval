import numpy as np
import pickle
document = {}

def create_place():
    print 'Create Place...'
    data = np.load('../../database/place.npy')
    for ele in data:
        file_name = str(ele[0].split('.')[0] + '.jpg')
        print 'Process attribute on %s' % file_name
        for word in ele[1:6]:
            word = word.replace('/', '_')
            word = word.replace(' ', '_')
            for w in word.split('_'):
                w = str(w)
                if document.has_key(file_name):
                    document[file_name] = document[file_name] + " " + w
                else:
                    document[file_name] = w

def create_attribute():
    print 'Create Attribute...'
    data = np.load('../../database/attribute.npy')
    for ele in data:
        file_name = str(ele[0].split('.')[0] + '.jpg')
        print 'Process attribute on %s' % file_name
        for word in ele[1:11]:
            word = word.replace('/', '_')
            word = word.replace(' ', '_')
            for w in word.split('_'):
                w = str(w)
                if document.has_key(file_name):
                    document[file_name] = document[file_name] + " " + w
                else:
                    document[file_name] = w

if __name__ == '__main__':
    create_place()
    create_attribute()
    pickle.dump(document, open('../document/place_attribute_document.pickle', 'wb'))
