import re
import pandas as pd

class Indexer:
    def __init__(self,initial_structure={}):
        self.indexed_words = initial_structure
    
    def getIndexed(self):
        return self.indexed_words

    def index(self,tokens, idx):

        for token in tokens:
            if token not in self.indexed_words.keys():
                self.indexed_words[token] = { idx : 1 }
            else:
                # get the dictionary that is a value of token
                value_dict = self.indexed_words[token]
                if idx not in value_dict.keys():
                    value_dict[idx] = 1
                else:
                    value_dict[idx] += 1
                self.indexed_words[token] = value_dict