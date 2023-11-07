"""Given a list of numbers, create a function that removes 25% from every number in the list except the smallest number, and adds the total 
amount removed to the smallest number.
Examples

show_the_love([4, 1, 4]) ➞ [3, 3, 3]

show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]

show_the_love([2, 100]) ➞ [27, 75]

Notes

There will only be one smallest number in a given list."""

def show_the_love(lst):
    #add = sum([i / 4 if i != min(lst) else 0 for i in lst])
    lst = [i - (i / 4) if i != min(lst) else i + sum(i / 4 if i != min(lst) else 0 for i in lst) for i in lst]
    return [int(i) if not i%1 else float(i) for i in lst]

print(show_the_love([4, 1, 4]))
print(show_the_love([16, 10, 8]))
print(show_the_love([2, 100]))

"""def show_the_love(lst):
    new = [i * 0.75 for i in lst]
    new[lst.index(min(lst))] += sum(lst) - sum(new)
    return new"""