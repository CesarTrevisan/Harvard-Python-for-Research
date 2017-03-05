# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 06:22:50 2017

@author: trevi
"""

from collections import Counter

text = "This is my test text. We're keeping this text short to keep this manageable"

def count_words(text):
    """Count the number of times that each word occurs on given string.
    Return a Dictionary where the keys are unique words and the value are word counts.
    Skip punctuaction.        
    
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', ]
    word_counts = {}
    for ch in skips:
        text = text.replace(ch, "")

    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
    
def count_words_fast(text):
    """Count the number of times that each word occurs on given string.
    Return a Dictionary where the keys are unique words and the value are word counts.
    Skip punctuaction.        
    
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', ]
    word_counts = {}
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))

    return word_counts
    
def read_book(title_path):
    """
    Read a Book and return it as a String.
    """
    
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    
    return text
    
def word_stats(word_counts):
    """
    Return the number unique words and frequency
    """
    
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique, counts)

    
import os
import pandas as pd

book_dir = "C:\\Users\\trevi\\Desktop\\python_case_studies\\Books"

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "\\" + language):
        for title in os.listdir(book_dir + "\\" + language + "\\" + author):
            inputfile = book_dir + "\\" + language + "\\" + author + "\\" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1
            
    
import matplotlib.pyplot as plt

plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")
    

plt.figure(figsize = (10,10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")  
    
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")

subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
    
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique Words")
plt.savefig("lang_plot.pdf")
    
    
    
    
    
    
    
    
    
    
    
    
    
    