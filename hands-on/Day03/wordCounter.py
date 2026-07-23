from collections import Counter
import re

print("--------------------------------------")
print("***********Word Counter***************")
print("--------------------------------------")

loop_countine = True
while(loop_countine):
	paragraph = input("Paste sentence to find the count of each word: ")
	lowercase_text = paragraph.lower()
	words = re.findall(r'\b\w+\b', lowercase_text)
	
	words_count = Counter(words)
	
	print("\nWord Counts:", dict(words_count), "\n")
	print("Most Common Words:", words_count.most_common(1))
	
	dyc = input("Do you want to continue further y/n: ")
	if dyc.lower() == 'y':
		loop_countine = True
	elif dyc.lower() == 'n':
		loop_countine = False
