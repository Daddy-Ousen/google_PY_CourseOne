from email.policy import strict
from unicodedata import name


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("big" > "small")

print(11 % 5)

def format_name(first_name, last_name):
    if first_name and last_name:
        return first_name + last_name
    elif first_name:
        return first_name
    elif last_name:
        return last_name
    else:
        return ""

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string



def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	elif len(word3) >= len(word1) and len(word3) >= len(word2):
		word = word3
	else:
		word = word1
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

print((10>=5*2) and (10<=5*2))



def fractional_part(numerator, denominator):
    if numerator == 0:
        return 0
    elif denominator == 0:
        return 0
    elif numerator % denominator > 0:
        return float(numerator % denominator) / denominator
    elif numerator % denominator < 0:
        return float(numerator % denominator) / denominator
    elif numerator % denominator == 0:
        return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

print("Week Two Is Done")