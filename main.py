from corpus_reader import Reader
from tokenizer import Tokenizer
from indexer import Indexer

import pandas as pd

class RTLI: #Reader, tokenizer, linguistic, indexer
    def __init__(self,file='content/all_sources_metadata_2020-03-13.csv'):
        self.reader = Reader(file)
        self.tokenizer = Tokenizer()
        self.indexer = Indexer()

    def process(self,tokenizer="simple"):

        # Reading step
        dataframe = self.reader.read_text() # This provides a pandas dataframe
        print(dataframe)


if __name__ == "__main__": #maybe option -t simple or -t complex
    rtli = RTLI()
    rtli.process()