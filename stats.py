def get_num_words(text):
	words = text.split()
	return len(words)

def get_char_frequency(text):
	chars = {}
	for char in text:
		char = char.lower()
		if char not in chars:
			chars[char] = 0
		chars[char] += 1
	return chars

def get_sorted_char_frequency(chars: dict):
	sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
	return sorted_chars
	