import sys
#from collections import OrderedDict

class Map:
    def __init__(self):
        self.intermediate = dict()
        #OrderedDict()
    

    def intermediateOutput(self, key, value):
        self.intermediate[key] = self.intermediate.get(key, 0) + value
        #self.intermediate.setdefault(key, 0)
        #self.intermediate[key] += 1


    def execute(self, data, mapper):
        mapper(data)
        

def read_input(file):
    line_number = 0
    print("Enter paragraphs")

    for line in file:
        line_number += 1
        yield line_number, line

        if line_number >= limit:
            return line_number, line
            raise StopIteration


def mapper(record):
    record = record.strip().split()

    for word in record:
        wordCountMap.intermediateOutput(word, 1)


wordCountMap = Map()

if __name__ == '__main__':
    limit = 500

    for line, inputData in read_input(sys.stdin):
        if line > limit:
            break
        wordCountMap.execute(inputData, mapper)
    
    for key, value in wordCountMap.intermediate.items():
        print(key, value)
