"""Given a predetermined rate from a dictionary, write the function that will return the time it takes for a certain amount of 
people to paint a certain amount of walls.

The "rate" dictionary shows how many minutes it takes "people" people to paint "walls" walls. At that same rate, how long should it 
take based on the new variables. Return the minutes as an integer. No rounding is necessary.
Example

# It takes 22 minutes for 10 people to paint 10 walls.
# How many minutes does it take 14 people to paint 14 walls?

rate = {
  "people": 10,
  "walls": 10,
  "minutes": 22
}

time(rate, people, walls) ➞ 22"""

def time(rate, people, walls):
    r = rate["minutes"] / rate["walls"] * rate["people"]
    return (r * walls) / people

rate1 = {
	'people': 4,
	 'walls': 9,
	 'minutes': 63 
}
rate2 = {
  'people': 10,
  'walls': 10,
  'minutes': 22
}

print(time(rate1, 7, 4)) #, 16)
print(time(rate2, 10, 10)) #, 22)

"""def time(dct, people, walls):
  return (dct['minutes'] * dct['people'] * walls) // (dct['walls'] * people)"""