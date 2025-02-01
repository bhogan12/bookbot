#returns count of words in a given text
def count_words(book_text):
    word_list = book_text.split()
    return len(word_list)

#returns a dictionary of character keys mapping to their values
def count_characters(book_text):
    character_list = list(book_text.lower())
    character_dict = {}

    for character in character_list:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    
    return character_dict

def print_report(book_text, dict):
    new_list = []

    #defines a key that tells .sort() to compare "num" values from the dictionary
    def sort_by(dict):
        return dict["num"]
    
    #creates list of dictionaries with character values and count values
    for char in dict:
        if char.isalpha():
            new_list.append({"char": char, "num": dict[char]})
    
    #sort using our defined comparison, reverse true so that highest values go first
    new_list.sort(key=sort_by, reverse=True) 

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book_text)} words found in the document")
    print("")
    
    for charcount in new_list:
        print(f"The '{charcount["char"]}' character was found {charcount["num"]} times")

    print("")
    print("--- End report ---")



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    word_count = count_characters(file_contents)
    print_report(file_contents, word_count)
            




main()

