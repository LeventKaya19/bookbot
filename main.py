def print_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    d = get_char_count_dict(file_contents)

    print(f"--- Begin report of {file_path} ---" )
    print(f"{len(d)} words found in the document")

    for key in d:
        print(f"The {key} character was found {d[key]} times")

def get_char_count_dict(file_contents):
    charDict = dict()

    lowered_strings = file_contents.lower().split()

    for s in lowered_strings:
        for c in s:
            if c in charDict:
                charDict[c] +=1
            else:
                charDict[c] = 1

    return charDict

    


def print_word_count(file_contents):
    words = file_contents.split()

    print(len(words))

def main():
    print_report("books/frankeinstein.txt")
    


main()