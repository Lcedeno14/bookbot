def openBooks(path):
    with open(path) as f:
        # reading frankenstein book
        file_contents = f.read()
        return file_contents
    
def main():
    bookPath = "books/frankenstein.txt"
    book = openBooks(bookPath)
    print(book)


main()