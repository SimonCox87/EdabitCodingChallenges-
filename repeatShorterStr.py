# Write a function that repeats the shorter string until it is equal to the length of the longer string.
# Examples

# lengthen("abcdefg", "ab") ➞ "abababa"

# lengthen("ingenius", "forest") ➞ "forestfo"

# lengthen("clap", "skipping") ➞ "clapclap"

# Notes

#     Both strings will differ in length.
#     Both strings will contain at least one character.
#     Either of the two strings could be the shortest in length.

def lengthen(s1,s2):
    l1,l2 = len(s1),len(s2)
    d = abs(l1-l2)
    return s2+(s2*(l1//l2))[:d] if l2<l1 else s1+(s1*(l2//l1))[:d]

print(lengthen("abcdefg", "ab")), "abababa"
print(lengthen("ingenius", "forest")), "forestfo"
print(lengthen("skipping", "clap")), "clapclap"
print(lengthen("k", "champagne")), "kkkkkkkkk"
print(lengthen("DUH", "champagne")), "DUHDUHDUH"

# def lengthen(s1, s2):
#     n = max(len(s1),len(s2))
#     return ((s1 if len(s1) < len(s2) else s2)*n)[:n]

# def lengthen(s1, s2):
#     n = len(max(s1, s2, key=len))
#     return (n * min(s1, s2, key=len))[:n]

