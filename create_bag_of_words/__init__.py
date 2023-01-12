import itertools

class Bow:

  def __init__(self, words, separator):

    self.__words = words
    self.__separator = separator

  def get_bag_of_words(self):

    lst_global = []

    for word in self.__words:

      word = word.lower().split(self.__separator)
      lst = [[i.title(), i] for i in word]
      lst_global.extend([" ".join(i) for i in list(itertools.product(*lst))])
      lst_global.extend(["-".join(i) for i in list(itertools.product(*lst))])

    return lst_global

if __name__ == '__main__':

  output = Bow(["Hello world Hi", "Shrikant shinde"], " ").get_bag_of_words()

  print(len(output))
  print(output)