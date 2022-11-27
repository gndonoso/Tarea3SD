#!/usr/bin python
# -*-coding:utf-8 -*

import sys

current_word = None
current_document = None
current_count = 0
total_word_data = []
word = None
f = open('output.txt','w')
for line in sys.stdin:
    line = line.strip()
    word, count, title = line.split('\t',2)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word and current_document == title:
        current_count += count
    else:
        if current_word == word:
            total_word_data.append((current_word,current_count,current_document))
        elif current_word != None:
            total_word_data.append((current_word,current_count,current_document))
            f.write(str(current_word)+":\t")
            for data in total_word_data:
                f.write("("+str(data[2])+", "+str(data[1])+") ")
            f.write('\n')
            total_word_data = []
        current_word = word
        current_document = title
        current_count = count


if current_word == word and current_document == title:
    total_word_data.append((current_word,current_count,current_document))
    f.write(str(current_word)+":\t")
    for data in total_word_data:
        f.write("("+str(data[2])+", "+str(data[1])+") ")
    f.write('\n')