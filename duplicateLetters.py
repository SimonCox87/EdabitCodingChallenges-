"""Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
Examples

no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".

Notes

Letter matches are case-insensitive."""

def no_duplicate_letters(phrase):
    return 2 not in [w.count(l) for w in phrase.lower().split() for l in w]

print(no_duplicate_letters("Easy does it.")) #True
print(no_duplicate_letters("So far, so good.")) #False
print(no_duplicate_letters("Better late than never.")) #False
print(no_duplicate_letters("Beat around the bush.")) #True
print(no_duplicate_letters("Give them the benefit of the doubt.")) #False
print(no_duplicate_letters("Your guess is as good as mine.")) #False
print(no_duplicate_letters("Make a long story short.")) #True
print(no_duplicate_letters("Go back to the drawing board.")) #True
print(no_duplicate_letters("Wrap your head around something.")) #True)
print(no_duplicate_letters("Get your act together.")) #False
print(no_duplicate_letters("To make matters worse.")) #False)
print(no_duplicate_letters("No pain, no gain.")) #True
print(no_duplicate_letters("We'll cross that bridge when we come to it.")) #False
print(no_duplicate_letters("Call it a day.")) #False
print(no_duplicate_letters("It's not rocket science.")) #False
print(no_duplicate_letters("A blessing in disguise.")) #False
print(no_duplicate_letters("Get out of hand.")) #True
print(no_duplicate_letters("A dime a dozen.")) #True
print(no_duplicate_letters("Time flies when you're having fun.")) #True
print(no_duplicate_letters("The best of both worlds.")) #True
print(no_duplicate_letters("Speak of the devil.")) #True
print(no_duplicate_letters("You can say that again.")) #False"""
print(no_duplicate_letters("Always be closing.")) #False

"""def no_duplicate_letters(phrase):
	return all(len(set(i)) == len(i) for i in phrase.split())"""

"""def no_duplicate_letters(phrase):
  return all(i.count(j)==1 for i in phrase.split() for j in i)"""
