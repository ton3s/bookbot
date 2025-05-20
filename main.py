from stats import get_num_words, get_char_frequency, get_sorted_char_frequency
import sys

def get_book_text(filepath):
	with open(filepath, "r") as file:
		return file.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	filepath = sys.argv[1]
	book_text = get_book_text(filepath)
	char_freq = get_char_frequency(book_text)
	sorted_char_freq = get_sorted_char_frequency(char_freq)
	
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(book_text)} total words")
	print("--------- Character Count -------")
	for char, freq in sorted_char_freq:
		print(f"{char}: {freq}")
	print("============= END ===============")

main()
