from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import numpy as np

document = {}
dictionary = []

def create_index():
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    ix = create_in("index", schema)
    writer = ix.writer()

    index_entity()
    index_action()
    index_place()
    index_attribute()

    print 'Indexing...'
    for key in document.keys():
        path_image = key
        concept = " ".join(list(set(document[key].split(" "))))
        writer.add_document(title=unicode(path_image, 'utf-8'), path=unicode(path_image, 'utf-8'), content=unicode(concept, 'utf-8'))

    writer.commit()

    np.save('dictionary', np.array(dictionary))

def index_entity():
    print 'Create Entity...'
    csv = open('../database/Entity.csv', 'r')
    for line in csv:
        array = line.split(',')
        file_name = str(array[0].split('/')[-1])
        dictionary.append(str(array[1]))
        if document.has_key(file_name):
            document[file_name] = document[file_name] + " " + str(array[1])
        else:
            document[file_name] = str(array[1])

def index_action():
    print 'Create Action...'
    data = np.load('../database/action.npy')
    for ele in data:
        file_name = str(ele[0])
        for word in ele[1:]:
            for w in word.split('_'):
                w = str(w)
                dictionary.append(w)
                if document.has_key(file_name):
                    document[file_name] = document[file_name] + " " + w
                else:
                    document[file_name] = w

def index_place():
    print 'Create Place...'
    data = np.load('../database/place.npy')
    for ele in data:
        file_name = str(ele[0].split('.')[0] + '.jpg')
        for word in ele[1:6]:
            word = word.replace('/', '_')
            word = word.replace(' ', '_')
            for w in word.split('_'):
                w = str(w)
                dictionary.append(w)
                if document.has_key(file_name):
                    document[file_name] = document[file_name] + " " + w
                else:
                    document[file_name] = w

def index_attribute():
    print 'Create Attribute...'
    data = np.load('../database/attribute.npy')
    for ele in data:
        file_name = str(ele[0].split('.')[0] + '.jpg')
        for word in ele[1:11]:
            word = word.replace('/', '_')
            word = word.replace(' ', '_')
            for w in word.split('_'):
                w = str(w)
                dictionary.append(w)
                if document.has_key(file_name):
                    document[file_name] = document[file_name] + " " + w
                else:
                    document[file_name] = w


if __name__ == '__main__':
    create_index()
