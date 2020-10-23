from corpus_reader import Reader
from tokenizer import Tokenizer
from indexer import Indexer
import time
from functools import reduce
import sys

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

    def domain_questions(self,time):
        # Question a)
        mem_size = sys.getsizeof(self.indexed_map) / 1024 / 1024
        print("A) Estimated process time: %.4fs and spent %.2f Mb of memory" % (time,mem_size))

        # Question b)
        vocab_size = len(self.indexed_map.keys())
        print("B) Vocabulary size is: %d" % (vocab_size))

        # Question c)
        ten_least_frequent = [ key for (key,value) in sorted(self.indexed_map.items(), key=lambda x: (len(x[1]), x[0]), reverse=False)[:10]] # i think we can do this, because these keys only have 1 value, which is the least possible to get inserted into the dict
        # sort alphabetical
        #ten_least_frequent.sort()
        print("\nC) Ten least frequent terms:")
        for term in ten_least_frequent:
            print(term)

        # Question d)
        ten_most_frequent = [ key for (key,value) in sorted(self.indexed_map.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)[:10]] # i think we can do this, because these keys only have 1 value, which is the least possible to get inserted into the dict
        # sort alphabetical
        #ten_most_frequent.sort()
        print("\nD) Ten most frequent terms:")
        for term in ten_most_frequent:
            print(term)

if __name__ == "__main__": #maybe option -t simple or -t complex
    
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <complex/simple>")
        sys.exit(1)
    
    tic = time.time()
    rtli = RTLI()

    if sys.argv[1] == "complex":
        rtli.process("complex")
    
    elif sys.argv[1] == "simple":
        rtli.process()
    
    else:
        print("Usage: python3 main.py <complex/simple>")
        sys.exit(1)
    
    toc = time.time()
    #print(rtli.indexed_map)
    rtli.domain_questions(toc-tic)