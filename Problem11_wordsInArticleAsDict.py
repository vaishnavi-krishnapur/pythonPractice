class Problem11():
    def __init__(self):
        self.word_freq={}

    def get_word_frequencies(self, filename, common_words):
        file=open(filename,'r')
        content=file.read()
        content=content.lower().split()
        #print(content)
        for i in content:
            if i not in common_words:
                if i not in self.word_freq:
                    self.word_freq[i]=1
                else:
                    self.word_freq[i] += 1
        file.close()
        return self.word_freq

    def get_n_most_frequent(self, word_freq,n):
        most_freq=[]
        word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1],reverse=True))
        for i in word_freq:
            tuple= (i,word_freq[i])
            most_freq.append(tuple)
            n -=1
            if n==0:
                break
        return most_freq
        

obj=Problem11()
common_words = ['is', 'a','the','an', 'for','at','it','in', 'of','or', 'to']
word_freq=obj.get_word_frequencies('Problem11_input.txt',common_words)
print(word_freq)
print(obj.get_n_most_frequent(word_freq,3))

