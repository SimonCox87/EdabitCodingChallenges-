"""And who cursed the most in the fight between you and your spouse?

Given a dict with three rounds, with nested dicts as your score per round, return who cursed the most based on the following:

    If you, return "ME!"
    If your spouse, return "SPOUSE!"
    If a draw, return "DRAW!"

Examples

determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 5, "spouse": 10 },
  "round3": { "me": 10, "spouse": 10 }}) ➞ "DRAW!"

determine_who_cursed_the_most({
  "round1": { "me": 40, "spouse": 5 },
  "round2": { "me": 9, "spouse": 10 },
  "round3": { "me": 9, "spouse": 10 }}) ➞ "ME!"

determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 9, "spouse": 44 },
  "round3": { "me": 10, "spouse": 55 }}) ➞ "SPOUSE!"

"""

def determine_who_cursed_the_most(d):
    c = sum(i["me"] - i["spouse"] for i in d.values())
    return "ME!" if c > 0 else "SPOUSE!" if c<0 else "DRAW!"

print(determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 5, "spouse": 10 },
  "round3": { "me": 10, "spouse": 10 }})) # ➞ "DRAW!"

print(determine_who_cursed_the_most({
  "round1": { "me": 40, "spouse": 5 },
  "round2": { "me": 9, "spouse": 10 },
  "round3": { "me": 9, "spouse": 10 }})) # ➞ "ME!"

print(determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 9, "spouse": 44 },
  "round3": { "me": 10, "spouse": 55 }})) # ➞ "SPOUSE!"

"""def determine_who_cursed_the_most(d):
	s=sum(v['me']-v['spouse']for v in d.values())
	return('DRAW!',('SPOUSE!','ME!')[s>0])[s!=0]"""
