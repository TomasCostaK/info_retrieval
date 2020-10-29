import re
import Stemmer
from corpus_reader import Reader
import time

class Tokenizer:
    def __init__(self):
        pass
    
    # Function to read any text and add it to the word dictionary of the Tokenizer
    def tokenize(self,input_string,index,stopwords,tokenizer_mode):
        final_tokens = []

        # we do the simple tokenizer
        if tokenizer_mode == "simple":
            tokens = re.sub("[^a-zA-Z]+"," ",input_string).lower().split(" ")

        # we go into the complex tokenizer
        else:
            tokens = re.sub("[^0-9a-zA-Z]+"," ",input_string).lower().split(" ") # Make some changes here, having into account that this is a biomedical corpus
            # Snowball stemmer - PyStemmer implementation
            stemmer = Stemmer.Stemmer('english')
            tokens = stemmer.stemWords(tokens)


        # Iterate over each word in line 
        for token in tokens: 
            # Disregard words with less than 3 chars, or if they are a stopword
            if len(token)<3 or token in stopwords: 
                continue

            # if it passes the condition, we shall add it to the final_tokens
            final_tokens.append((token,index))
        
        return final_tokens


"""
if __name__ == "__main__":
    word_dict = {}
    tic = time.time()
    tokenizer = Tokenizer(word_dict)

    tokenizer.tokenize('content/all_sources_metadata_2020-03-13.csv')
    toc = time.time()
    print("Estimated time: %.3f s" % (toc-tic))
    #print(tokenizer.word_counter())
    print(tokenizer.top_x_words(3))
"""