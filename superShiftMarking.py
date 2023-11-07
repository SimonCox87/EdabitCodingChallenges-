# Given a dictionary of student names and a list of their test scores over the semester, return a list of all the students who 
# passed the course (in alphabetical order). However, there is one more thing to mention: the pass mark is 100% in everything!

# Examples

# who_passed({
#   "John" : ["5/5", "50/50", "10/10", "10/10"],
#   "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
#   "Adam" : ["8/10", "22/25", "3/5", "5/5"],
#   "Barry" : ["3/3", "20/20"]
# }) ➞ ["Barry", "John"]

# who_passed({
#   "Zara" : ["10/10"],
#   "Kris" : ["30/30"],
#   "Charlie" : ["100/100"],
#   "Alex" : ["1/1"]
# }) ➞ ["Alex", "Charlie", "Kris", "Zara"]

# who_passed({
#   "Zach" : ["10/10", "2/4"],
#   "Fred" : ["7/9", "2/3"]
# }) ➞ []

# Notes

#     All of a student's test scores must be 100% to pass.
#     Remember to return a list of student names alphabetically.

def who_passed(students):
    val = zip(students.keys(),[all([eval(i)==1 for i in students[j]]) for j in students.keys()])
    return sorted(i[0] for i in val if i[1])

print(who_passed({
  "John" : ["5/5", "50/50", "10/10", "10/10"],
  "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
  "Adam" : ["8/10", "22/25", "3/5", "5/5"],
  "Barry" : ["3/3", "20/20"]
})) # ➞ ["Barry", "John"]

print(who_passed({
  "Zara" : ["10/10"],
  "Kris" : ["30/30"],
  "Charlie" : ["100/100"],
  "Alex" : ["1/1"]
})) # ➞ ["Alex", "Charlie", "Kris", "Zara"]

print(who_passed({
  "Zach" : ["10/10", "2/4"],
  "Fred" : ["7/9", "2/3"]
})) # ➞ []

# def who_passed(students):
# 	return sorted(name for name, grades in students.items() if all(eval(i) == 1 for i in grades))

# def who_passed(students):
# 	return sorted([s for s in students if all(map(lambda x:x==1,[eval(i) for i in students[s]]))])