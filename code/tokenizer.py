import re
import Stemmer
from corpus_reader import Reader
import time

class Tokenizer:
    def __init__(self):
        self.token_dict = {}

    # Function to read any text and add it to the word dictionary of the Tokenizer
    def tokenize(self,input_string,tokenizer_mode):
        final_tokens = []

        # we do the simple tokenizer
        if tokenizer_mode == "simple":
            tokens = re.sub("[^a-zA-Z]+"," ",input_string).lower().split(" ")
            stopwords = []

        # we go into the complex tokenizer
        else:
            tokens = re.sub("[^0-9a-zA-Z]+"," ",input_string).lower().split(" ") # Make some changes here, having into account that this is a biomedical corpus
            # Snowball stemmer - PyStemmer implementation
            stemmer = Stemmer.Stemmer('english')
            tokens = stemmer.stemWords(tokens)

            # Include stopwords in a list, and then not add word if its one of stopwords
            text = open('../content/snowball_stopwords_EN.txt','r')
            stopwords = [word.strip() for word in text.readlines()]

        # Iterate over each word in line 
        for token in tokens: 
            # Disregard words with less than 3 chars, or if they are a stopword
            if len(token)<3 or token in stopwords : 
                continue

            # if it passes the condition, we shall add it to the final_tokens
            final_tokens.append(token)

            if token in self.token_dict: 
                # Increment count of token by 1 
                self.token_dict[token] = self.token_dict[token] + 1
            else: 
                # Add the token to dictionary with count 1 
                self.token_dict[token] = 1
        
        return final_tokens

    # Function to return the most frequent words with the texts that have been fed to the Tokenizer
    def word_counter(self):
        return sorted(self.token_dict.items(), key=lambda x: x[1])

    # Pass an integer to get top X tokens in a text
    def top_x_words(self,stopping):
        return sorted(self.token_dict.items(), key=lambda x: x[1])[-stopping:]

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