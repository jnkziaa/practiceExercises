# read content
print("Write a function in python to read the content from a text file 'poem.txt' line by line and display the same "
      "on screen.\n")


def poem_reader():
    r = open("poem.txt", 'r', encoding='utf-8')
    output_poem = r.read()
    r.close()
    return output_poem


print(poem_reader())

# count number of lines
print("\n------------------------------------------------------------------------------------------------------------")
print("2. Write a function in python to count the number of lines from a text file 'story.txt' which is not starting "
      "with an alphabet 'T' ")


def line_counter():
    with open('story.txt') as f:
        lines = f.readlines()
    print(lines)
    _count = 0
    for i in range(len(lines)):
        if lines[i][0] != 'T':
            _count += 1

    return _count


print("The count of lines not starting with 'T' = ", line_counter())

# count and dispay
print("\n------------------------------------------------------------------------------------------")
print("Write a function in Python to count and display the total number of words in a text file.")


def count_and_display():
    with open('story.txt') as f:
        __words = f.read()
    _count = __words.split()
    print(_count)
    return len(_count)


print("Number of words = ", count_and_display())

# occurences of the word the
print("\n------------------------------------------------------------------------------------------")
print("Write a function in Python to read lines from a text file 'notes.txt'. Your function should find and display "
      "the occurrence of the word 'the'.")


def count_word_the():
    with open('notes.txt') as f:
        __words = f.read()
    _split = __words.split()
    _count = 0
    result = []
    for i in range(len(_split)):
        temp = _split[i]
        if temp.lower() == 'the':
            result.append(i)
            _count += 1
    print("Word 'the' occurred in word : ", result)
    return _count


print(count_word_the())

# less than 4 characters
print("\n------------------------------------------------------------------------------------------")
print("Write a function display_words() in python to read lines from a text file 'story.txt', and display those "
      "words, which are less than 4 characters.")


def display_words():
    with open('story.txt') as f:
        __words = f.read()
    _split = __words.split()
    _count = 0
    result = []
    for i in range(len(_split)):
        temp = _split[i]
        if len(temp) < 4:
            result.append(temp)
            _count += 1

    print("Results are : ", result)
    return _count


print(display_words(), "words are less than 4 characters")

# count_these_this
print("\n------------------------------------------------------------------------------------------")
print('Write a function in Python to count the words "this" and "these" present in a text file "article.txt". [Note '
      'that the words "this" and "these" are complete words]')


def count_this_these():
    with open('article.txt') as f:
        __words = f.read()
    _split = __words.split()
    _count = 0
    _result = []
    for i in range(len(_split)):
        temp = _split[i]
        if temp.lower() == 'this':
            _result.append(i)
            _count += 1
        elif temp.lower() == 'these':
            _result.append(i)
            _count += 1
    print("This or these occured in line : ", _result)
    return _count


print("These or this occured : ", count_this_these(), "times")

# alphabet 'e'
print("\n------------------------------------------------------------------------------------------")
print('Write a function in Python to count words in a text file those are ending with alphabet "e". ')


def ending_with_e():
    with open('poem.txt') as f:
        __words = f.read()
    _split_words = __words.split()
    _count = 0
    _result = []
    for i in range(len(_split_words)):
        temp = _split_words[i]
        if temp.lower()[len(temp) - 1] == 'e':
            _result.append(temp)
            _count += 1

    print("This or these occured in line : ", _result)
    return _count


print("Word ended with 'e' : ", ending_with_e(), "times")


# uppercase
print("\n------------------------------------------------------------------------------------------")
print('Write a function in Python to count uppercase character in a text file.')


def count_upper():
    with open('story.txt') as f:
        __words = f.read()
    _count = 0
    _result = []
    for i in range(len(__words)):
        temp = __words[i]
        if temp.isupper():
            _result.append(temp)
            _count += 1

    print("Upper Case : ", _result)
    return _count


print("Upper Case showed up : ", count_upper(), "times")

