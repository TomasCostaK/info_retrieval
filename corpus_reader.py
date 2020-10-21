import re
import pandas as pd

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):
        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]

        str_abstract = my_df['abstract'].str.cat(sep=' ')
        str_titles = my_df['title'].str.cat(sep=' ')
        str_final = str_abstract + " " + str_titles # there must a way prettier way to do this

        words = re.sub("[^0-9a-zA-Z]+"," ",str_final).lower().split(" ")
        return words
    
    def read_complex_text(self):

        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]

        str_abstract = my_df['abstract'].str.cat(sep=' ')
        str_titles = my_df['title'].str.cat(sep=' ')
        str_final = str_abstract + " " + str_titles # there must a way prettier way to do this
        
        words = str_final.lower().split(" ")

        return words