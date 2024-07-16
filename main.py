def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        word_count = countWords(file_contents)
        char_count = countCharacters(file_contents)
        print(f"--- Begin report of {file} ---")
        print(f"{word_count} words found in the document")
        sort(char_count)
        print("--- End report ---")

def countWords(string):
    words = string.split()
    word_count = len(words)
    return word_count

def countCharacters(string):
    character_count = dict()
    string = string.lower()
    for word in string:
        for char in word:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_on(dict):
    return (dict["count"])

def sort(dict):
    sorted =[]
    for entry in dict:
        if entry.isalpha():
            sorted.append({"letter": entry, "count": dict[entry]})
    sorted.sort(reverse=True, key=sort_on)
    for entry in sorted:
        print(f"The '{entry["letter"]}' character was found {entry["count"]} times")

main()