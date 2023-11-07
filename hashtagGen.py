# Create a function that is a Hashtag Generator by using the following rules:

#     The output must start with a hashtag (#).
#     Each word in the output must have its first letter capitalized.
#     If the final result, a single string, is longer than 140 characters, the function should return false.
#     If either the input (str) or the result is an empty string, the function should return false.

# Examples

# generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"

# generate_hashtag("") ➞ false, "Expected an empty string to return false"

# generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."

def generate_hashtag(txt):
    txt = "".join(txt.title().split())
    return False if len(txt)==0 or len(txt)>=140 else "#"+txt    

print(generate_hashtag("    Hello     World   " )) # ➞ "#HelloWorld"
print(generate_hashtag("")) # ➞ false, "Expected an empty string to return false"
print(generate_hashtag("Edabit Is Great")) # ➞ "#EdabitIsGreat", "Should remove spaces."

print(generate_hashtag("")) #, False, "Expected an empty string to return False")
print(generate_hashtag(" " * 100)) #, False, "Still an empty string")
print(generate_hashtag("Do We have A Hashtag")) #, "#DoWeHaveAHashtag", "Expected a Hashtag (#) at the beginning.")
print(generate_hashtag("Edabit")) #, "#Edabit", "Should handle a single word.")
print(generate_hashtag("Edabit Is Great")) #, "#EdabitIsGreat", "Should remove spaces.")
print(generate_hashtag("Edabit is great")) #, "#EdabitIsGreat", "Should capitalize first letters of all words.")
print(generate_hashtag("eda" + " " * 140 + "bit")) #, "#EdaBit")
print(generate_hashtag("Smmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaalllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll Dog")) #, False, "Should return False if the final word is longer than 140 chars.")
print(generate_hashtag("e" * 121)) #, "#E" + "e" * 120, "Should work")
print(generate_hashtag("e" * 140)) #, False, "Too long")
print(generate_hashtag("    Hello     World   " )) #, "#HelloWorld")

# def generate_hashtag(txt):
# 	txt = txt.title().replace(" ", "")
# 	return '#' + txt if 0 < len(txt) < 140 else False

# def generate_hashtag(txt):
# 	r = "".join(txt.title().split(" "))
# 	return "#" + r if r and len(r)<140 else False

# def generate_hashtag(txt):
# 	txt = txt.title().replace(' ', '')
# 	return '#' + txt if 1 <= len(txt) < 140 else False