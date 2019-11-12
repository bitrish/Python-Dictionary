import json
data=json.load(open("data1.json"))
data= {k.lower(): v for k, v in data.items()}
word=input("this is an open dictionary ,enter a word to find its meaning")
word=word.lower()
def translate(w):
    li = data[w]
    for x in range(len(li)):
        print(li[x])
from difflib import get_close_matches
cdata=get_close_matches(word,data.keys())[0]
if cdata==word:
    translate(cdata)
elif cdata!="":
    bol=input("no word found,did u mean the word " +cdata+" if yes enter y else enter n")
    if bol.lower()=="y":
        translate(cdata)

else:
    print("this word doesnt exit,please check your word")










