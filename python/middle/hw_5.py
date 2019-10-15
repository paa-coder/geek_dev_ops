from itertools import groupby

class Word:
    text=None
    part=None

    def __init__(self,text,part):
        self.text=text
        self.part=part


word_1 = Word("привет","глагол")

class Sentence:
    content = [0,1,2]

    def __init__(self,content = False):
        if content:
            self.content=content

    def show(self,words):
        for i in self.content:
            if i< len(words) and i>=0:
                print(words[i].text,end=" ")
        print("")

    def show_parts(self,words):
        list = []
        for i in self.content:
            if i< len(words) and i>=0 and words[i].part not in list:
                list.append(words[i].part)
        return list


words = [ Word(*i) for i in [["собака", "сущ"],["ела", "глагол"],["колбасу", "сущ"],["вечером", "наречие"]]]


sentense = Sentence()

sentense.show(words)

print(sentense.show_parts(words))
