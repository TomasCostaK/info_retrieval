from corpus_reader import Reader
from tokenizer import Tokenizer
from indexer import Indexer

import pandas as pd

class RTLI: #Reader, tokenizer, linguistic, indexer
    def __init__(self,file='content/all_sources_metadata_2020-03-13.csv'):
        self.reader = Reader(file)
        self.tokenizer = Tokenizer()
        self.indexer = Indexer()
        self.indexed_map = {}

    def process(self,tokenizer_mode="simple"):

        # Reading step
        dataframe = self.reader.read_text() # This provides a pandas dataframe
        
        # for each row in the datafram we will tokenize and index
        for index, row in dataframe.iterrows(): 

            # Tokenizer step
            appended_string = row['abstract'] + " " + row['title']
            tokens = self.tokenizer.tokenize(appended_string,tokenizer_mode=tokenizer_mode)

            print(tokens)
            # Indexer step
            """
            self.indexed_map = self.indexer(tokens)
            for word in words:
                if word not in words_map.keys():
                    #words_map[word] = [index] if index != None else index #deal with nans here
                    words_map[word] = [index]
                else:
                    words_map[word] += [index]
            """



if __name__ == "__main__": #maybe option -t simple or -t complex
    rtli = RTLI()
    rtli.process()