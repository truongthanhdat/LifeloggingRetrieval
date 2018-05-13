import json
from nltk.corpus import wordnet as wn
import pickle

document = {}

def parse_neural_talk():
    data = json.load(open('../../database/vis.json', 'r'))

    for element in data:
        file_path = element['file_name'].split('/')[-1]
        print 'Process NeuralTalk on %s' % file_path
        caption = element['caption']
        exists = {}
        for word in caption.split():
            candidates = wn.synsets(word)
            for candidate in candidates:
                if candidate.pos() == 'v':
                    name = candidate.name().split('.')[0]
                    if exists.has_key(name):
                        continue
                    exists[name] = True
                    if document.has_key(file_path):
                        document[file_path] = document[file_path] + " " + name
                    else:
                        document[file_path] = name

def parse_captions():
    data = open('../../database/Captions.txt', 'r').read().split('\n')
    for line in data:
        element = line.split('\t')
        file_path = element[0] + '.jpg'
        print 'Process Captions on %s' % file_path
        caption = " ".join(element[1:])
        exists = {}
        for word in caption.split():
            candidates = wn.synsets(word)
            for candidate in candidates:
                if candidate.pos() == 'v':
                    name = candidate.name().split('.')[0]
                    if exists.has_key(name):
                        continue
                    exists[name] = True
                    if document.has_key(file_path):
                        document[file_path] = document[file_path] + " " + name
                    else:
                        document[file_path] = name

if __name__ == '__main__':
    parse_neural_talk()
    parse_captions()
    pickle.dump(document, open('../document/action_document.pickle', 'wb'))
