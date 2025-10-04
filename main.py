import sys
inp_check = sys.argv
if len(inp_check) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]
from stats import get_number_of_words
from stats import get_number_of_charaters
from stats import sort_charaters

def main():

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}")
    print ("----------- Word Count ----------")
    print (f"Found {get_number_of_words(filepath)} total words")
    print ("--------- Character Count -------")
    FF = get_number_of_charaters(filepath)
    FL = sort_charaters(FF)
    for char, number in FL:
        print (f'{char}: {number}')
    print ("============= END ===============")


main()
