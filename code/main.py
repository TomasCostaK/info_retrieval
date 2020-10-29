from corpus_reader import Reader
from tokenizer import Tokenizer
from indexer import Indexer
import time
import sys
import os
import csv


class RTLI:  # Reader, tokenizer, linguistic, indexer
    def __init__(self, tokenizer_mode, file='../content/all_sources_metadata_2020-03-13.csv', stopwords_file="../content/snowball_stopwords_EN.txt", chunksize=10000):
        self.reader = Reader(file)
        self.tokenizer = Tokenizer(tokenizer_mode, stopwords_file)
        self.indexer = Indexer()

        # defines the number of lines to be read at once
        self.chunksize = chunksize

        # tryout for new structure in dict
        self.indexed_map = {}


    def gen_chunks(self, reader):
        chunk = []
        for i, line in enumerate(reader):
            if (i % self.chunksize == 0 and i > 0):
                yield chunk
                del chunk[:]  # or: chunk = []
            chunk.append(line)
        yield chunk

    def process(self):

        # Reading step
        #dataframe = self.reader.read_text() # This provides a pandas dataframe
        tokens = []
        
        # for each row in the datafram we will tokenize and index
        tic = time.time()

        with open('../content/all_sources_metadata_2020-03-13.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for chunk in self.gen_chunks(reader):
                for row in chunk:
                    index = row['doi']
                    # Tokenizer step
                    if row['abstract'] != "":
                        appended_string = row['abstract'] + " " + row['title']
                        tokens += self.tokenizer.tokenize(appended_string, index)
            
                toc = time.time()
                print("Estimated tokenizing/stemming time: %.4fs" % (toc-tic))

                tic = time.time()
                self.indexer.index(tokens, index)
                toc = time.time()
                print("Estimated indexing time: %.4fs" % (toc-tic))

        self.indexed_map = self.indexer.getIndexed()

    def domain_questions(self, time):
        # Question a)
        mem_size = self.calculate_dict_size(self.indexed_map) / 1024 / 1024
        print("A) Estimated process time: %.4fs and spent %.2f Mb of memory" %
              (time, mem_size))

        # Question b)
        vocab_size = len(self.indexed_map.keys())
        print("B) Vocabulary size is: %d" % (vocab_size))

        # Question c)
        # i think we can do this, because these keys only have 1 value, which is the least possible to get inserted into the dict
        ten_least_frequent = [key for (key, value) in sorted(
            self.indexed_map.items(), key=lambda x: (len(x[1]), x[0]), reverse=False)[:10]]
        # sort alphabetical
        #ten_least_frequent.sort()
        print("\nC) Ten least frequent terms:")
        for term in ten_least_frequent:
            print(term)

        # Question d)
        # i think we can do this, because these keys only have 1 value, which is the least possible to get inserted into the dict
        ten_most_frequent = [key for (key, value) in sorted(
            self.indexed_map.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)[:10]]
        # sort alphabetical
        #ten_most_frequent.sort()
        print("\nD) Ten most frequent terms:")
        for term in ten_most_frequent:
            print(term)

    def calculate_dict_size(self, input_dict):
        mem_size = 0
        for key, value in input_dict.items():
            # in python they dont count size, so we have to do it iteratively
            mem_size += sys.getsizeof(value)

        # adding the own dictionary size
        return mem_size + sys.getsizeof(input_dict)


if __name__ == "__main__":  # maybe option -t simple or -t complex

    if len(sys.argv) < 3:
        print("Usage: python3 main.py <complex/simple> <chunksize>")
        sys.exit(1)

    if sys.argv[1] == "complex":
        rtli = RTLI(tokenizer_mode="complex",chunksize=int(sys.argv[2]))

    elif sys.argv[1] == "simple":
        rtli = RTLI(tokenizer_mode="simple",chunksize=int(sys.argv[2]))

    else:
        print("Usage: python3 main.py <complex/simple>")
        sys.exit(1)

    tic = time.time()
    rtli.process()
    toc = time.time()

    rtli.domain_questions(toc-tic)
