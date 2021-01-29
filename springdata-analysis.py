import time
from textblob import TextBlob

file = open('Spring2020responses.csv', 'r')
out = open('out-spring.csv', 'w')

score = 0


out.write('Sentiment,Subjectivity,Text' + '\n')

for sentence in file:
    blob = TextBlob(sentence.rstrip())
    score = blob.sentiment.polarity
    sentence = sentence.replace('"', "'")
    out.write(str(score) + ',' +
              str(blob.sentiment.subjectivity) + ',' + '"' + str(sentence.rstrip()) + '"' + '\n')

out.close()
