"""Create a function based on the input and output. Look at the examples, there is a pattern.
Examples

secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"

Notes

Input is a string."""

def secret(txt):
    tag = ""
    start = 0
    for i in txt:
        if i != ".":
            tag += i
            start += 1
        else:
            break
    return "<"'{}'" class='".format(tag) + " ".join(txt[start:].split(".")).strip() + "'></"'{}'">".format(tag)

"""def secret(txt):
    tag, *class_name = txt.split(".")
    return "<{} class='{}'></{}>".format(tag, " ".join(class_name), tag)"""


print(secret("p.one.two.three"))
print(secret("p.one"))
print(secret("p.four.five"))
print(secret("h3.one"))
print(secret("h1.a.b.c.d"))
print(secret("h455.one.two.three"))