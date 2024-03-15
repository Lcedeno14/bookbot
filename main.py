def openBooks(path):
    with open(path) as f:
        # reading frankenstein book
        file_contents = f.read()
        return file_contents
def addAlphabetDictionary():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = {}
    for letter in alphabet:
        letters[letter] = 0
    return letters
def countBook(book):
    bookSplit = book.split()
    #bookWords = len(bookSplit)
    letters_dict = {}
    for words in bookSplit:
        for letters in words:
            letter=letters.lower()
            if letter in letters_dict:
                letters_dict[letter] = letters_dict[letter] + 1
            else:
                letters_dict[letter] = 1
    return letters_dict
    
def main():
    bookPath = "books/frankenstein.txt"
    book = openBooks(bookPath)
    wordCount = countBook(book)
    print(wordCount)
    


main()