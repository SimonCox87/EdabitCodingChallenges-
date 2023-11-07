"""Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list 
(where N is the length of the list).

Examples

majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

Notes

    The frequency of the majority element must be strictly greater than 1/2.
    If there is no majority element, return None.
    If the list is empty, return None."""

def majority_vote(lst):
    slst = sorted(list({i if lst.count(i) > len(lst) / 2 else "None" for i in lst}))
    return slst[0] if len(slst) > 0 and slst[0] != "None" else None

print(majority_vote(["A", "B", "B", "B", "A", "A"]))
print(majority_vote(["B", "B", "B"]))
print(majority_vote(["A", "B", "B"]))
print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
print(majority_vote(["A", "B"]))
print(majority_vote(["A"]))
print(majority_vote([]))


""""Test.assert_equals(majority_vote(["A", "B", "B", "B", "A", "A"]), None)
Test.assert_equals(majority_vote(["B", "B", "B"]), "B")
Test.assert_equals(majority_vote(["A", "B", "B"]), "B")
Test.assert_equals(majority_vote(["A", "A", "B"]), "A")
Test.assert_equals(majority_vote(["A", "A", "A", "B", "C", "A"]), "A")
Test.assert_equals(majority_vote(["B", "A", "B", "B", "C", "A", "B", "B"]), "B")
Test.assert_equals(majority_vote(["A", "B", "B", "A", "C", "C"]), None)
Test.assert_equals(majority_vote(["A", "B"]), None)
Test.assert_equals(majority_vote(["A"]), "A")
Test.assert_equals(majority_vote([]), None)"""

"""def majority_vote(lst): 
  for i in set(lst):
    if lst.count(i)>len(lst)//2:
      return i
  return None"""

print(0.5 ** (11 - 15 **2) + (1- 7 ** 2))
