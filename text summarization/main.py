from flask import Flask, render_template,request
import requests
from bs4 import BeautifulSoup
import nltk 
import pandas as pd

app = Flask(__name__)

def get_wiki_content(url):
    req_obj = requests.get(url)
    text = req_obj.text
    soup = BeautifulSoup(text)
    all_paras = soup.find_all("p")
    wiki_text = ''
    for para in all_paras:
        wiki_text += para.text 
    return wiki_text

def top10_sent(url):
    required_text = get_wiki_content(url)
    stopwords = nltk.corpus.stopwords.words("english")
    sentences = nltk.sent_tokenize(required_text)
    words = nltk.word_tokenize(required_text)
    word_freq = {}
    for word in words:
        if word not in stopwords:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    
    max_word_freq = max(word_freq.values())
    for key in word_freq.keys():
        word_freq[key] /= max_word_freq
    
    sentences_score = []
    for sent in sentences:
        curr_words = nltk.word_tokenize(sent)
        curr_score = 0
        for word in curr_words:
            if word in word_freq:
                curr_score += word_freq[word]
        sentences_score.append(curr_score)

    sentences_data = pd.DataFrame({"sent":sentences, "score":sentences_score})
    sorted_data = sentences_data.sort_values(by = "score", ascending = False).reset_index()

    top10_rows = sorted_data.iloc[0:11,:]
    
    #top_10 = list(sentences_data.sort_values(by = "score",ascending = False).reset_index().iloc[0:11,"sentences"])
    return " ".join(list(top10_rows["sent"]))

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        url_content = top10_sent(url)
        return url_content
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)