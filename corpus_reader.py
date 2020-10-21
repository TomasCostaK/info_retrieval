import re
import pandas as pd

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):
        words = []
        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]
        print(my_df['abstract'])
        """
        text = open(self.path,'r')
        for line in text: 
            words.extend(re.sub("[^a-zA-Z]+"," ",line).lower().split(" "))
        """
        return ["words"]
    
    def read_complex_text(self):
        words = []
        text = open(self.path,'r')
        for line in text: 
            words.extend(re.sub(""," ",line).lower().split(" ")) #here find a better solution

        return words