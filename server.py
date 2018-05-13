from flask import request, Flask
from flask_cors import CORS
import pickle
import difflib
from nltk.corpus import wordnet as wn
from whoosh import index as widx
from whoosh.qparser import QueryParser
import whoosh.qparser as qparser
import numpy as np

app = Flask(__name__)
CORS(app)

print 'Loading Indexing...'
ix = widx.open_dir('../indexing/index')
print 'Finish Loading...'
word_list = list(set(np.load('../indexing/document/dictionary.npy').tolist()))
print 'Dictionary has %d words' % len(word_list)

print 'Mapping image path to id'
npy_img_id = np.load('../database/path_to_id.npy')
map_img_path_to_id = {}
for ele in npy_img_id:
    key = ele.keys()[0]
    img_path = key.split('/')[-1]
    map_img_path_to_id[img_path] = ele[key]

string = '%s,%s,1.0\n'

@app.route('/search')
def api_search():
    if 'text' in request.args:
        return search(request.args['text'])
    return 'NULL'

def search(text):
    csv = open('result.csv', 'a')
    correct_words = []
    #topic_id = text.split("_")[0]

    for word in text.split('_'):
        correct_word = difflib.get_close_matches(word, word_list)
        if len(correct_word) == 0:
            continue
        correct_words.append(correct_word[0])

    text = " ".join(correct_words)
    img_path = []
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(text)
        results = searcher.search(query, limit=1000) #, group=qparser.OrGroup)
        for res in results:
            img_path.append(res['path'].split('/')[-1])
        img_path.sort()

    #for i_path in img_path:
    #    if not map_img_path_to_id.has_key(str(i_path)):
    #        continue
    #    s = map_img_path_to_id[str(i_path)]
    #    print s
    #    csv.write(string % (topic_id, s))

    if len(img_path) == 0:
        return "NULL"
    else:
        return text + "\n" + " ".join(img_path)

if __name__ == '__main__':
    app.run()
