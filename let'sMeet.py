# From point A, an object is moving towards point B at constant velocity va (in km/hr). From point B, another object is moving towards 
# point A at constant velocity vb (in km/hr). Knowing this and the distance between point A and B (in km)) #, write a function that returns 
# how much time passes until both objects meet.

# Format the output like this:

# "2h 23min 34s"

# Examples

# lets_meet(100, 10, 30) ➞ "2h 30min 0s"

# lets_meet(280, 70, 80) ➞ "1h 52min 0s"

# lets_meet(90, 75, 65) ➞ "0h 38min 34s"

# Notes

# Seconds should be rounded down to the nearest whole number.
# from math import floor

# def lets_meet(distance, va, vb):
#     time = distance / (va + vb)
#     hour = str(time)[:str(time).index(".")]
    
#     if time % 1:
#         mins = 60 * float(str(time)[str(time).index("."):])
    
#     if mins % 1:
#         secs = floor(60 * float(str(mins)[str(mins).index("."):]))
#     else:
#         secs = 0
    
#     return hour + "h " + str(floor(mins)) + "min " + str(secs) + "s"
  
    #     mins = int(mins)
    #     secs = int(secs)
    # return str(hour) + "." + str(mins) + "." + str(secs)

# print(lets_meet(100, 10, 30)) # ➞ "2h 30min 0s"
# print(lets_meet(280, 70, 80)) # ➞ "1h 52min 0s"
# print(lets_meet(90, 75, 65)) # ➞ "0h 38min 34s"

# print(lets_meet(100, 10, 30)) #, "2h 30min 0s")
# print(lets_meet(33, 15, 20)) #, "0h 56min 34s")
# print(lets_meet(250, 60, 80)) #, "1h 47min 8s")
# print(lets_meet(125, 55, 40)) #, "1h 18min 56s")
# print(lets_meet(0.6, 10, 15)) #, "0h 1min 26s")
# print(lets_meet(0.8, 23, 18)) #, "0h 1min 10s")
# print(lets_meet(0.72, 8, 12)) #, "0h 2min 9s")
# print(lets_meet(33, 15, 20)) #, "0h 56min 34s")
# print(lets_meet(360, 80, 64)) #, "2h 30min 0s")
# print(lets_meet(10, 45, 42)) #, "0h 6min 53s")
# print(lets_meet(90, 75, 65)) #, "0h 38min 34s")
# print(lets_meet(280, 70, 80)) #, "1h 52min 0s")

def lets_meet(distance, va, vb):
    t = distance / (va + vb)
    m = 60 * float(str(t)[str(t).index("."):])
    s = int(60 * float(str(m)[str(m).index("."):]))
    return'{}h {}min {}s'.format(str(t)[:str(t).index(".")], int(m), s)

print(lets_meet(100, 10, 30)) #, "2h 30min 0s")
print(lets_meet(33, 15, 20)) #, "0h 56min 34s")
print(lets_meet(250, 60, 80)) #, "1h 47min 8s")
print(lets_meet(125, 55, 40)) #, "1h 18min 56s")
print(lets_meet(0.6, 10, 15)) #, "0h 1min 26s")
print(lets_meet(0.8, 23, 18)) #, "0h 1min 10s")
print(lets_meet(0.72, 8, 12)) #, "0h 2min 9s")
print(lets_meet(33, 15, 20)) #, "0h 56min 34s")
print(lets_meet(360, 80, 64)) #, "2h 30min 0s")
print(lets_meet(10, 45, 42)) #, "0h 6min 53s")
print(lets_meet(90, 75, 65)) #, "0h 38min 34s")
print(lets_meet(280, 70, 80)) #, "1h 52min 0s")

# def lets_meet(distance, va, vb):
# 	t = int(3600*distance/(va+vb))
# 	return '{}h {}min {}s'.format(t//3600,(t%3600)//60,t%60)

# def lets_meet(distance, va, vb):
#     seconds=(distance/(va+vb))*3600
#     m, s = divmod(seconds, 60)
#     h, m = divmod(m, 60)
#     return '{}h {}min {}s'.format(int(h), int(m), int(s))