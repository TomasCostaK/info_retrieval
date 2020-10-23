import re
from corpus_reader import Reader
import time

class Tokenizer:
    def __init__(self):
        self.word_dict = {}

    # Function to read any text and add it to the word dictionary of the Tokenizer
    def tokenize(self,path):

        reader = Reader(path)
        words = reader.read_text()

        # Iterate over each word in line 
        for word in words: 
            # Check if the word is already in dictionary 
            if len(word)<3: # is this enough?
                continue
            
            if word in self.word_dict: 
                # Increment count of word by 1 
                self.word_dict[word] = self.word_dict[word] + 1
            else: 
                # Add the word to dictionary with count 1 
                self.word_dict[word] = 1

    # Function to return the most frequent words with the texts that have been fed to the Tokenizer
    def word_counter(self):
        return sorted(self.word_dict.items(), key=lambda x: x[1])

    # Pass an integer to get top X words in a text
    def top_x_words(self,stopping):
        return sorted(self.word_dict.items(), key=lambda x: x[1])[-stopping:]


if __name__ == "__main__":
    word_dict = {}
    tic = time.time()
    tokenizer = Tokenizer(word_dict)

    tokenizer.tokenize('content/all_sources_metadata_2020-03-13.csv')
    toc = time.time()
    print("Estimated time: %.3f s" % (toc-tic))
    #print(tokenizer.word_counter())
    print(tokenizer.top_x_words(3))