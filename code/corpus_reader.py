import re
import pandas as pd

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):
        my_df = pd.read_csv(self.path)
        my_df = my_df[my_df.abstract.notnull()]

        return my_df
