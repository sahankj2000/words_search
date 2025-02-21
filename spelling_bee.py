
if __name__ == '__main__':
    optional_letters = input("Enter all the optional letters(grey): ")
    required_letters = input("Enter the required letters(yellow): ")
    print("Searching for minimum length of 4")
    min_length = 4
    with open('words_alpha.txt', 'r') as file:
        all_words = file.readlines()
    print("Words that match the criteria:")
    for word in all_words:
        word = word.strip()
        if len(word) < min_length:
            continue
        has_required = True
        for required_letter in required_letters:
            if required_letter not in word:
                has_required = False
                break
        if has_required:
            rest_are_only_optionals = True
            for word_letter in word:
                if word_letter not in optional_letters and word_letter not in required_letters:
                    rest_are_only_optionals = False
                    break
            if rest_are_only_optionals:
                print(word)
