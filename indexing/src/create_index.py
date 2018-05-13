from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import pickle
import argparse
import os
import progressbar
import time

def parse_args():
    parser = argparse.ArgumentParser('Creading Inverted Index')
    parser.add_argument('--document', help='Path to document', type=str, required=True)
    parser.add_argument('--index_dir', help='Path to index dir', type=str, required=True)
    parser.add_argument('--list_path', help='Path to list', type=str, default=None)
    return parser.parse_args()

def create_index(document, index_dir):
    d = time.time()

    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    print 'Indexing %s' % index_dir
    keys = document.keys()
    for i in progressbar.progressbar(range(len(keys))):
        key = keys[i]
        path_image = key
        concept = " ".join(list(set(document[key].split(" "))))
        writer.add_document(title=unicode(path_image, 'utf-8'), path=unicode(path_image, 'utf-8'), content=unicode(concept, 'utf-8'))

    print 'Committing into %s' % index_dir
    writer.commit()
    d = time.time() - d
    print 'Finish! Indexing take %f second' % d

if __name__ == '__main__':
    options = parse_args()
    document = pickle.load(open(options.document, 'rb'))
    create_index(document, options.index_dir)

