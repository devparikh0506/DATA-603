from mrjob.job import MRJob
class WordCountJob(MRJob):
     def mapper(self, _, line):
         for word in line.split():
            if word:
                formatted_word = ''.join(letter for letter in word.lower() if letter.isalnum()).strip()
                if len(formatted_word) > 0:
                    yield(formatted_word, 1)

     def reducer(self, word, counts):
         yield(word, sum(counts))


if __name__ == '__main__':
    WordCountJob.run()
