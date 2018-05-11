from flask import request, Flask
from flask_cors import CORS
import pickle
import difflib
from nltk.corpus import wordnet as wn

app = Flask(__name__)
CORS(app)

ivt = pickle.load(open("inverted_index.pickle", "rb"))
word_list = ivt.keys()

@app.route('/search')
def api_search():
    if 'text' in request.args:
        return search(request.args['text'])
    return 'NULL'

def search(text):
    correct_word = difflib.get_close_matches(text, word_list)
    if (len(correct_word) == 0):
        return "NULL";
    correct_word = correct_word[0]
    candidate_words = [str(word.name().split('.')[0]) for word in wn.synsets(correct_word)]
    words = [word for word in candidate_words if ivt.has_key(word)]
    words = list(set(words))
    result = []
    for word in words:
        result = result + ivt[word]
    if len(result) == 0:
        return "NULL"
    else:
        return " ".join(words) + "\n" + " ".join(result)

if __name__ == '__main__':
    app.run()
