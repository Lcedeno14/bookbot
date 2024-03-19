def openBooks(path):
    with open(path) as f:
        # reading frankenstein book
        file_contents = f.read()
        return file_contents
    
def wordCount(book):  
    bookSplit = book.split()
    bookWords = len(bookSplit)
    return bookWords  

def countBook(book):
    letters_dict = {}
    for words in book:
        for letters in words:
            letter=letters.lower()
            if letter in letters_dict:
                letters_dict[letter] = letters_dict[letter] + 1
            else:
                letters_dict[letter] = 1
    return letters_dict

def sorter(dictionary):
    return dictionary["num"]

def sortDict(dictionary):
    dictToList = []
    for letters in dictionary:
        dictToList.append({"letter":letters, "num":dictionary[letters]})
    dictToList.sort(key = sorter,reverse = True)
    return dictToList

def printLetters(dictionary):
    for letters in dictionary:
        if letters["letter"].isalpha():
            print(f"The '{letters["letter"]}' character was found {letters["num"]} times")


def main():
    bookPath = "books/frankenstein.txt"
    book = openBooks(bookPath)
    letterCount = countBook(book)
    sortedLetterList = sortDict(letterCount)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount(book)} words found in the document\n")
    printLetters(sortedLetterList)
    print(f"--- End report ---")

main()