import sys

class Reduce:
    def __init__(self):
        self.word_dict = dict()

    
    def suffle(self, key, value):
        self.word_dict[key] = self.word_dict.get(key, 0) + value


    def execute(self, data, reducer):
        reducer(data)


def reducer(pair):
    wordCountReducer.suffle(pair[0], int(pair[1]))


def mapper_output_reader(file):
    for pairs in file:
        yield pairs.strip().split()


wordCountReducer = Reduce()

if __name__ == '__main__':

    for key, value in mapper_output_reader(sys.stdin):
        wordCountReducer.execute((key, value), reducer)
    print(wordCountReducer.word_dict)
