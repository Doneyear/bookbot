def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    number_words = get_num_words(file_contents)
    number_letter = get_num_letters(file_contents)
    number_letter.sort(reverse=True, key=sort_dict)
    report = ""
    report += f"{number_words} words found in the document\n\n"
    for entry in number_letter:
        report += f"The '{entry['char']} character was found {entry['num']} times \n"
    print(report)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    dict_list = []
    for l in text:
        if l.isalpha():
            lowered = l.lower()
            if lowered in letters:
                letters[lowered] += 1
            else: letters[lowered] = 1
    for letter, count in letters.items():
        entry = {'char': letter, 'num': count}
        dict_list.append(entry)
    return dict_list

def sort_dict(dict):
    return dict["num"]

if __name__ == "__main__":
    main()