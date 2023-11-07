"""Tidy Hyperlinks

Using markdown, it's possible to format links such as https://edabit.com/challenges, into something tidier like this. Notice how 
the text "Go to the challenges!" appears when hovering over the link.

This was achieved by using this code:

[this](https://edabit.com/challenges "Go to the challenges!")

Given the url, the new name and optionally the hover_text, return the tidied up hyperlink as a string.
Examples

tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!") ➞ "[this](https://edabit.com/challenges "Go to the 
challenges!")"

tidy_link("https://www.google.com", "Google", "Google Search") ➞ "[Google](https://www.google.com "Google Search")"

tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!") ➞ "[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"

Notes

    Supply double quotes for the hover text.
    Keep in mind that some tests will not include an argument for hover_text."""

def tidy_link(url, name, hover_text = ""):
    return '\'[{1}]({0} "{2}")\''.format(url, name, hover_text) if hover_text != "" else '\'[{1}]({0})\''.format(url, name)
print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
print(tidy_link("https://www.g1oogle.com", "Google", "Google Search"))
print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))
print(tidy_link('https://edabit.com/challenges', 'Challenges', 'Go to the challenges!'))
print(tidy_link('https://www.google.com', 'Google', 'Google Search'))
print(tidy_link('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Click Me!'))
print(tidy_link('https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet', 'Markdown Cheatsheet'))
print(tidy_link('https://www.python.org/', 'Python', 'Visit the Python Website!'))
print(tidy_link('https://www.youtube.com/watch?v=O2yPnnDfqpw', 'i just did a bad thing'))
print(tidy_link('https://www.reddit.com/', 'Reddit', 'the front page of reddit'))

"""def tidy_link(url, name, hover_text):
    return f'[{name}]({url}) "{hover_text}'
print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))
print(tidy_link("https://www.google.com", "Google", "Google Search"))
print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))"""

"""('https://edabit.com/challenges', 'Challenges', 'Go to the challenges!'), '[Challenges](https://edabit.com/challenges "Go to the challenges!")')
('https://www.google.com', 'Google', 'Google Search'), '[Google](https://www.google.com "Google Search")')
('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Click Me!'), '[Click Me!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)')
('https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet', 'Markdown Cheatsheet'), '[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)')
('https://www.python.org/', 'Python', 'Visit the Python Website!'), '[Python](https://www.python.org/ "Visit the Python Website!")')
('https://www.youtube.com/watch?v=O2yPnnDfqpw', 'i just did a bad thing'), '[i just did a bad thing](https://www.youtube.com/watch?v=O2yPnnDfqpw)')
('https://www.reddit.com/', 'Reddit', 'the front page of reddit'), '[Reddit](https://www.reddit.com/ "the front page of reddit")')"""

'[Challenges](https://edabit.com/challenges "Go to the challenges!")'

def tidy_link(url, name, hover_text=""):
    return '[{}]({} "{}")'.format(name, url, hover_text) if hover_text else '[{}]({})'.format(name, url)