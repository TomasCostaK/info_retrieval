import re
import pandas as pd

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):
        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]

        return my_df

        for index, row in my_df.iterrows(): 
            str_abstract = row['abstract']
            str_titles = row['title']
            str_final = str_abstract + " " + str_titles # there must a way prettier way to do this

            words = re.sub("[^a-zA-Z]+"," ",str_final).lower().split(" ")

            #print("\nGoing for Document %s\n" % (index))

            for word in words:
                if word not in words_map.keys():
                    #words_map[word] = [index] if index != None else index #deal with nans here
                    words_map[word] = [index]
                else:
                    words_map[word] += [index]
