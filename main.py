def main():
    # path location to the book's text file
    path = "books/frankenstein.txt"

    try:
        with open(path) as f:
            file_contents = f.read().lower()
            # print(file_contents)
            letters = letter_frequency(file_contents)

            # to sort in descending order of total occurrence
            letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
            print_report(path, file_contents, letters)
    except:
        print("Something went wrong. Please check if you have added the text file to the correct location.")
        print("[Hint: Please check the book path provided in the MAIN function.]")

def print_report(path, content, letters):
    print(f"--- Begin report of {path} ---")
    print(len(content.split()), "words found in the document\n")

    # printing detailed report only for alphabetical characters
    for i in letters:
        if 97<=ord(i)<97+26:
            print(f"The '{i}' character was found {letters[i]} times")
    print("--- End report ---")

def letter_frequency(bookstring):
    letters = {}
    for i in bookstring:
        if i not in letters: letters[i] = 1
        else: letters[i]+=1
    return letters

if __name__=="__main__":
    main()