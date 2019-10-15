from itertools import groupby

class Word:
    text=None
    __part=None
    __grammar="сущ"

    def __init__(self,text,part,grammar):
        self.text=text
        self.__part=part
        self.__grammar = grammar

    def part(self):
        return self.__part


class Noun(Word):
    def __init__(self,text):
        super(Noun,self).__init__(text,"существительное","сущ")

class Verb(Word):
    def __init__(self,text):
        super(Verb,self).__init__(text,"глагол","гл")

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
            if i< len(words) and i>=0 and words[i].part() not in list:
                list.append(words[i].part())
        return list


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))


sentense = Sentence()

sentense.show(words)

print(sentense.show_parts(words))
