def get_book_text(path="books/frankenstein.txt"):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text.lower():
        letters[letter] = letters.get(letter, 0) + 1
    return letters

def sort_on(dict):
    return dict["value"]

def dict_to_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"key": key, "value": dict[key]})
    return dict_list

def main():
    text = get_book_text()
    char_dict = (count_letters(text))
    char_dict_list = dict_to_list(char_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print("-------- Report Starts --------")
    for item in char_dict_list:
        if item["key"].isalpha():
            print(f"The letter {item['key']} appears {item['value']} times")
    print("-------- Report Ends --------")
main()