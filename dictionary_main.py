import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))


def word_meaning(words):
    # word_small = words.lower()
    # word_title = words.title()
    if words.lower() in data:
        return data[words.lower()]
    elif words.title() in data:
        return data[words.title()]
    elif words.upper() in data:
        return data[words.upper()]

    else:
        try:
            my_list = get_close_matches(words, data)
            ratio_list = []
            for w in my_list:
                check = SequenceMatcher(None, words, w).ratio()
                ratio_list.append(check)
            suit_word_val = max(ratio_list)
            suit_word_index = ratio_list.index(suit_word_val)
            suit_word = my_list[suit_word_index]
            print(f'Did you mean {suit_word}?\nEnter y or n')
            if input() == 'y':
                return data[suit_word]
            else:
                return 'Word not found'
        except KeyError:
            return 'Word doesnt exist. Please check the spelling!'


while True:
    print('Enter word to search or q to quit:')
    word = input()
    # word = word.lower()
    if word != 'q':
        try:
            print_word = word_meaning(word)
            if type(print_word) == list:
                for item in print_word:
                    print(item)
            else:
                print(print_word)
        except:
            print('Please check the input')
    else:
        break
