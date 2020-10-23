from corpus_reader import Reader
from tokenizer import Tokenizer
from indexer import Indexer
import time
from functools import reduce

import pandas as pd

class RTLI: #Reader, tokenizer, linguistic, indexer
    def __init__(self,file='../content/all_sources_metadata_2020-03-13.csv'):
        self.reader = Reader(file)
        self.tokenizer = Tokenizer()
        self.indexer = Indexer()

        # tryout for new structure in dict
        self.indexed_map = {}

    def process(self,tokenizer_mode="simple"):

        # Reading step
        dataframe = self.reader.read_text() # This provides a pandas dataframe
        
        # for each row in the datafram we will tokenize and index
        for index, row in dataframe.iterrows(): 

            # Tokenizer step
            appended_string = row['abstract'] + " " + row['title']
            tokens = self.tokenizer.tokenize(appended_string,tokenizer_mode=tokenizer_mode)

            # Indexer step
            self.indexer.index(tokens, index)    

        self.indexed_map = self.indexer.getIndexed()

if __name__ == "__main__": #maybe option -t simple or -t complex
    tic = time.time()
    rtli = RTLI()
    rtli.process()
    toc = time.time()
    print(rtli.indexed_map)

    print("Estimated time: %.4f s" % (toc-tic))