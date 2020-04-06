import requests
import pandas as pd


titleId = pd.read_table(r"C:\Users\rahul\OneDrive\Desktop\title.akas.tsv")["titleId"]

titleIdUnique = titleId.unique()[:10]

def get_data(url):
    response = requests.get(url)
    json = response.json()
    return [json["Metascore"], json["imdbRating"], json["imdbVotes"], json["BoxOffice"], json["Production"]]

data_list = []
for titleId in titleIdUnique:
    url = "http://www.omdbapi.com/?i={0}&apikey=c6f94d42".format(titleId)
    data_list.append(get_data(url))

dataFrame = pd.DataFrame(data_list, columns = ["Metascore", "imdbRating", "imdbVotes", "BoxOffice", "Production"])

print(dataFrame)
    
