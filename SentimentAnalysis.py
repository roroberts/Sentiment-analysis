# a program that uses textblob library with pip to perform sentiment and subjectivity analysis
# positive and negative sentiments reflected quantitatively
# can read .csv or .text files and still write .csv files

import time
from textblob import TextBlob

file = open('Fall2020 Q12_Text.csv', 'r')
out = open('out-fall.csv', 'w')
# clean up the files first; .txt or .csv work;
# drag and drop the files into VScode then revise the file = open name above accordingly
# the file is the fall2020 comments on the
# student experience survey in SurveyMonkey in response to question 12
score = 0


out.write('Sentiment,Subjectivity,Text' + '\n')

for sentence in file:
    blob = TextBlob(sentence.rstrip())
    score = blob.sentiment.polarity
    sentence = sentence.replace('"', "'")
    out.write(str(score) + ',' +
              str(blob.sentiment.subjectivity) + ',' + '"' + str(sentence.rstrip()) + '"' + '\n')

out.close()
# the program will write a .csv file that can be copied through dragging and dropping
# text library from text blob: https://textblob.readthedocs.io/en/dev/
# questions: how to best summarize the quantitative data: average? median? mean? max?
# can revise to


# next: analyze data in Python: https://scipy.org/about.html
