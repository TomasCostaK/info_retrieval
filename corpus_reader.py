import re
import pandas as pd

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):
        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]
        words_map = {}

        for index, row in my_df.iterrows(): 
            str_abstract = row['abstract']
            str_titles = row['title']
            str_final = str_abstract + " " + str_titles # there must a way prettier way to do this

            words = re.sub("[^0-9a-zA-Z]+"," ",str_final).lower().split(" ")

            
            for word in words:
                if word not in words_map.keys():
                    #words_map[word] = [row['sha']] if row['sha'] != None else index #deal with nans here
                    words_map[word] = [index]
                else:
                    lista= words_map[word]
                    print(lista)
                    words_map[word] = lista.extend(lista)
            
            print(words_map)
        
        return words
    
    def read_complex_text(self):

        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]

        str_abstract = my_df['abstract'].str.cat(sep=' ')
        str_titles = my_df['title'].str.cat(sep=' ')
        str_final = str_abstract + " " + str_titles # there must a way prettier way to do this
        
        words = str_final.lower().split(" ")

        return words