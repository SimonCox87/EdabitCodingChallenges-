# Create a function that takes a list of students and returns a dictionary representing their notes distribution. Keep in mind that 
# invalid notes should not be counted in the distribution. Valid notes are: 1, 2, 3, 4, 5

# Example

# get_notes_distribution([
#   {
#     "name": "Steve",
#     "notes": [5, 5, 3, -1, 6]
#   },
#   {
#     "name": "John",
#     "notes": [3, 2, 5, 0, -3]
#   }
# ] ➞ {
#   5: 3,
#   3: 2,
#   2: 1
# })

def get_notes_distribution(students):
    notes = [j for i in [n["notes"] for n in students] for j in i if j>0 and j<6]
    return {i: notes.count(i) for i in notes}

print(get_notes_distribution([
    {
        "name": "Steve",
        "notes": [5, 5, 3, -1, 6]
    },
    {
        "name": "John",
        "notes": [3, 2, 5, 0, -3]
    }
])) 
# # ➞ {
# 5: 3,
# 3: 2,
# 2: 1
# }))

# def get_notes_distribution(students):
# 	notes = sum([i['notes'] for i in students], [])
# 	return {i: notes.count(i) for i in set(notes) if 1 <= i <= 5}

