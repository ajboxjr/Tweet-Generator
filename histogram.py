import sys
import time
import random

class Histogram(dict):
    def __init__(self, source_text=None):
        self.source_text = source_text
        if self.source_text:
            self.histogram()
        self.tuple = self.to_tuple()
        self.list = self.to_list()

    def unique_words(self):
        unique_arr = []
        for key , val in self.items():
            if val == 1:
                unique_arr.append(key)
        #print("Unique words: {}".format(unique_arr))
        return unique_arr

    def frequency(self, word):
        if word in self:
            print("{}: {}".format(word, self[word]))
            return self[word]
            
    def histogram(self):
        for word in self.source_text:
            if word in self: 
                self[word] += 1
            else:
                self[word] =1
    def add_count(self, word, count=1):
        if word in self:
            self[word] += count
        else:
            self[word] = count

    def getName(self,item):
        return item[0]

    def getCount(self, item):
        return item[1]

    def sort(self,option):
        if option == 'word':
            return sorted(self.tuple, key=self.getName)
        if option == 'count':
            return sorted(self.tuple, key=self.getCount)

    def stochastic(self):
        for i in range(len(self.tuple)):
            print(tup_histogram[i][0])

    def to_list(self):
        list_histogram = []
        for key,val in self.items():
            list_histogram.append([key,val])
        return list_histogram

    def to_tuple(self):
        tuple_histogram = []
        for key,val in self.items():
            tuple_histogram.append((key,val))
        #print(tuple_histogram)
        return tuple_histogram

    def export_histogram(self, histogram_title):
        file =  open(histogram_title+'.txt', 'w')
        for key, val in self.items():
            string = "{} {}\n".format(key,val)
            file.write(string)
        file.close()

def read_text(file_name):
    with open(file_name) as f:
       return f.read().split()

def handle_input(input_word):
    if input_word.endswith('.txt'):
        print('input a text file:' + input_word)
        source_text = read_text(input_word) 
        print(source_text)
        return source_text
    else:
        print("input raw string \n")
        return input_word.split()
def time_diffrence(start_time):
    total_time = time.time()-start_time
    return total_time
if __name__ == '__main__':
    source_text = " ".join(sys.argv[1:])
    time_start = time.time()
    histogramz = Histogram(handle_input(source_text))
    histogramz.frequency('fish')
    print(histogramz.to_tuple())
    print(histogramz.to_list())
    print(time_diffrence(time_start))
