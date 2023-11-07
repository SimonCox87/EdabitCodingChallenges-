"""A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the 
tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
Examples

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2"""

def tallest_skyscraper(lst):
    counter = 0
    for list in lst:
        for item in list:
            counter += 1
    
    highest = 0
    tower = 0
    row = 0
    column = 0
    divisor = len(lst)

    while counter != 0:
        tower += lst[row][column]
        row += 1
        counter -= 1
        if counter % divisor == 0:
            column += 1
            row = 0
            if tower > highest:
                highest = tower
            tower = 0
    return highest

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))

print(tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))

print(tallest_skyscraper([
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]
]))

def tallest_skyscraper(lst):
    return max([sum(x) for x in zip(*lst)])

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))

"""def tallest_skyscraper(lst):
	return sum(1 for i in lst if sum(i)>0)

def tallest_skyscraper(A):
	return sum(1 in R for R in A)

def tallest_skyscraper(lst):
    return len([row for row in lst if 1 in row])"""