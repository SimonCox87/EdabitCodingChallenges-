# Suppose a student can earn 100% on an exam by getting the answers all correct or all incorrect. Given a potentially incomplete 
# answer key and the student's answers, write a function that determines whether or not a student can still score 100%. Incomplete 
# questions are marked with an underscore, "_".

# ["A", "_", "C", "_", "B"]   # answer key
# ["A", "D", "C", "E", "B"]   # student's solution

# ➞ True

# # Possible for student to get all questions correct.

# ["B", "_", "B"]   # answer key
# ["B", "D", "C"]   # student's solution

# ➞ False

# # First question is correct but third is wrong, so not possible to score 100%.

# ["T", "_", "F", "F", "F"]   # answer key
# ["F", "F", "T", "T", "T"]   # student's solution

# ➞ True

# # Possible for student to get all questions incorrect.

# Examples

# possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True

# possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True

# possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False

# possibly_perfect(["B", "_"], ["C", "A"]) ➞ True

# possibly_perfect(["B", "A"], ["C", "A"]) ➞ False

# possibly_perfect(["B"], ["B"]) ➞ True

# Notes

# Test has at least one question.

def possibly_perfect(key, answers):
    nK = [k == a for k, a in zip(key, answers) if k != "_"]
    return sum(nK) in (0,len(nK))
                                                                                


# print(possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"])) #  ➞ True
# print(possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"])) # ➞ True
# print(possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"])) # ➞ False
# print(possibly_perfect(["B", "_"], ["C", "A"])) # ➞ True
# print(possibly_perfect(["B", "A"], ["C", "A"])) # ➞ False
# print(possibly_perfect(["B"], ["B"])) # ➞ True

print(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B'])) # True)
print(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C'])) # False)
print(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T'])) # True)

print(possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C'])) # True)
print(possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C'])) # True)
print(possibly_perfect(['A', 'B', 'C', '_'], ['B', 'A', 'C', 'C'])) # False)

print(possibly_perfect(['B', '_'], ['C', 'A'])) # True)
print(possibly_perfect(['B', 'A'], ['C', 'A'])) # False)
print(possibly_perfect(['B'], ['B'])) # True)

print(possibly_perfect(['_', 'T', '_', '_'], ['T', 'F', 'F', 'F'])) # True)
print(possibly_perfect(['_', 'T', '_', '_'], ['T', 'T', 'F', 'T'])) # True)
print(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'F', 'T'])) # False)
print(possibly_perfect(['_', 'T', 'T', 'T'], ['T', 'T', 'T', 'T'])) # True)
print(possibly_perfect(['_', 'T', 'T', 'T'], ['F', 'F', 'F', 'F'])) # True)

# def possibly_perfect(k, a):
# 	return len(set(i==j for i,j in zip(k,a) if i!="_"))==1