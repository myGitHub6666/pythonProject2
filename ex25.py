def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """sorts  the two words """
    return sorted(words)


def print_first_words(words):
    """ print the first words after popping it off"""
    words = words.pop(0)
    print(words)


def print_last_words(words):
    """prints the last words after popping it off """
    words = words.pop(-1)
    print(words)


def sort_sentence(sentence):
    """"takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_fist_and_last(sentence):
    """prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_words(words)
    print_last_words(words)


def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)


stu = input("<<<")
# 列表中可以保存多种类型的数据吗？？？？
# stu = [1,2,3,'g','j']
print(break_words(stu))
print("___________________")
print(sort_words(stu))
print("*************************")
'''<<<asdhjaskfh1432
['1', '2', '3', '4', 'a', 'a', 'd', 'f', 'h', 'h', 'j', 'k', 's', 's']'''
# print_first_words(stu)
# print_last_words(stu)
print(sort_sentence(stu))






