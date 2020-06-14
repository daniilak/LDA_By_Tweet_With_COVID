# /usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys
import peewee
import argparse
import pandas as pd
import nltk
import re

from nltk.corpus import stopwords
from pymystem3 import Mystem
from lib.DataBase import DataBase, IntegrityError, OperationalError
from models.words import Words

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-f', '--file', default='covid_tweets.csv.gz')
    parser.add_argument ('-o', '--offset', default=0)
 
    return parser
        
        
nltk.download("stopwords")
mystem = Mystem() 

db = DataBase()
try:
    try:
        db.open_connection()
    except (peewee.OperationalError):
        print("connection")
except (IntegrityError, OperationalError):
    db = DataBase()
    db.open_connection()

file_name = 'covid_tweets.csv.gz'
nrows = 0 + 30000

russian_stopwords = stopwords.words("russian")


dataSet = pd.read_csv(file_name, nrows=nrows, compression='gzip', error_bad_lines=False)

idx = 0
count = len(dataSet['text'])

for text in dataSet['text']:
    sys.stdout.write('\r')
    tokens = mystem.lemmatize(re.sub(r'[^а-яА-Я ]', '', text).lower())
    
    for token in tokens:
        token = token.strip()
        if token not in russian_stopwords and token != " " and len(token) > 0:
            row = Words(
                word=token,
            )
            row.save(force_insert=True)
    idx += 1
    sys.stdout.write("[%-20s] %d%% loaded" %('='*int(idx*20/count), idx*100/count))
    
print("\nini DONE!\n")

