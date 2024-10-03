from mrjob.job import MRJob
import re
import enchant

class NonEngWordCount(MRJob):

    def __init__(self, *args, **kwargs):
        super(NonEngWordCount, self).__init__(*args, **kwargs)
        self.d = enchant.Dict("en_US")

    def mapper(self, _, line):
        for word in line.split():
            if word:
                formatted_word = ''.join(letter for letter in word.lower() if letter.isalnum()).strip() 
                if formatted_word  and len(formatted_word) > 0 and not self.d.check(formatted_word):
                    yield(formatted_word, 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    NonEngWordCount.run()
