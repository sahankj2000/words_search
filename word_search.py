#!/usr/bin/env python3
import json


def is_my_pattern(pattern):
    for character in pattern:
        if str.isalpha(character) is True or character == '.':
            continue
        else:
            return False
    return True


def my_pattern_match(pattern, string, weak_match = False):
    """
    weak_match is for ignore patterns
    """
    if len(pattern) != len(string) or is_my_pattern(pattern) is False or str.isalpha(string) is False:
        return False
    pattern, string = str.lower(pattern), str.lower(string)
    for i, character in enumerate(pattern):
        if weak_match:
            if character != '.' and character == string[i]:
                return True
        else:
            if character != '.' and character != string[i]:
                return False
    if weak_match:
        return False
    return True


def search(word_length, search_pattern, ignore_letters, include_letters, ignore_patterns):
    print(f'----------Prompt----------\nWord Length: {word_length},\nSearch Pattern: \'{search_pattern}\',\nIgnore Letters: {ignore_letters},\nInclude Letters: {include_letters},\nIgnore Patterns: {ignore_patterns}')
    sample, words_alpha, words = 'sample.txt', 'words_alpha.txt', 'words.txt'
    with open(words_alpha) as file:
        print(f'Searching in file: \'{file.name}\'\n----------Output----------')
        lines = file.readlines()
        for i, line in enumerate(lines):
            line = str.lower(line.strip())
            if line != '' and str.isalpha(line) and len(line) == word_length:
                if search_pattern.strip() != '':
                    result = my_pattern_match(search_pattern, line.strip(), False)
                    if result is False:
                        continue
                skip = False
                for letter in line:
                    if letter in ignore_letters:
                        skip = True
                        break
                if skip:
                    continue
                for letter in include_letters:
                    if letter not in line:
                        skip=True
                        break
                if skip:
                    continue
                for ignore_pattern in ignore_patterns:
                    if my_pattern_match(ignore_pattern, line, True) is True:
                        skip = True
                        break
                if not skip:
                    print(line)

def get_splitted_letters(letters):
    splitted_letters = []
    for letter in str.lower(letters):
        if letter.strip() != '':
            splitted_letters.append(letter)
    return splitted_letters


if __name__ == '__main__':
    """
    Disclaimer the two words list files are from: https://github.com/dwyl/english-words
    word_length: length of word
    search_pattern: pattern to look for, '.' for any letter eg: '.aha.', no wild card (### green letters and rest dots)
    ignore_letters: add letters you know are not in the word (### greyed out letters)
    include_letters: add letters that you know are in the word, but position is unknown (### orange letters)
    ignore_patterns: patterns that should be ignored even if they have include_letters (### orange letters and rest dots)
    """
    file = open('prompt.json')
    data = json.load(file)
    word_length = data['word_length']
    search_pattern = str.lower(data['search_pattern']).strip()
    ignore_letters = get_splitted_letters(data['ignore_letters'])
    include_letters = get_splitted_letters(data['include_letters'])
    ignore_patterns = data['ignore_patterns']
    remove_from_ignore = []
    for letter in ignore_letters:
        if letter in search_pattern:
            remove_from_ignore.append(letter)
    for letter in remove_from_ignore:
        print(f'\n!!! WARN: Removing \'{letter}\' from ignore_letters as it is found in pattern')
        ignore_letters.remove(letter)
    search(word_length, search_pattern, ignore_letters, include_letters, ignore_patterns)

