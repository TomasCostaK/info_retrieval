import re
import pandas as pd
import csv

class Reader:
    def __init__(self,file):
        self.path = file
    
    def read_text(self):

        with open(self.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
        
        csvfile.close()
        
        #my_df = pd.read_csv(self.path)
        #my_df = my_df[my_df.abstract.notnull()]

        return reader
