# In this challenge, you must build a function that inflects an infinitive regular Italian verb of the first conjugation form to the 
# present tense, including the personal subjective pronoun.

# All first conjugation Italian verbs share the same suffix: ARE. The first thing to do is separate the verb root from the suffix.

#     Root of "programmare" (to code) = "programm".
#     Root of "giocare" (to play) = "gioc".

# For each subjective pronoun the root is combined with a new suffix: see table below (pronouns are numbered for coding ease, in real 
# grammar they are grouped in singular and plural, both from first to third):
# #	Pronoun	Suffix
# 1	Io (I)	o
# 2	Tu (You)	i
# 3	Egli (He)	a
# 4	Noi (We)	iamo
# 5	Voi (You)	ate
# 6	Essi (They)	ano

#     Present tense of verb "parlare" (to speak) for third pronoun:
#         Pronoun ("Egli") + Root ("parl") + Suffix ("a") = "Egli parla".
#     Present tense of verb "lavorare" (to work) for fourth pronoun:
#         Pronoun ("Noi") + Root ("lavor") + Suffix ("iamo") = "Noi lavoriamo".

# There are two exceptions for present tense inflection:

#     If root ends with "c" or "g" the second and fourth pronoun suffixes add a "h" at the start:
#         "Attaccare" (to attack) = "Tu attacchi" (instead of "Tu attacci")
#         "Legare" (to tie) = "Noi leghiamo" (instead of "Noi legiamo")
#     If root ends with "i" the second and fourth pronoun suffixes lose the starting "i" (so that second pronoun suffix disappears):
#         "Inviare" (to send) = "Noi inviamo" (instead of "Noi inviiamo")
#         "Tagliare" (to cut) = "Tu tagli" (instead of "Tu taglii")
#         "Mangiare" (to eat) = "Noi mangiamo" (instead of "Noi mangiiamo")
#         "Cacciare" (to hunt) = "Tu cacci" (instead of "Tu caccii")

# Given a string verb being the infinitive form of the first conjugation Italian regular verb, and an integer pronoun being the 
# subjective personal pronoun, implement a function that returns the inflected form as a string.
# Examples

# conjugate("programmare", 5) ➞ "Voi programmate"

# conjugate("iniziare", 2) ➞ "Tu inizi"

# conjugate("mancare", 4) ➞ "Noi manchiamo"

# Notes

#     In the returned string, pronouns must be capitalized and verbs must be in lowercase, separated by a space between them.
#     Curious fact: first conjugation (verbs ending in "are") is also called "the living conjugation", because every new verb that 
#     enters the Italian dictionary is assigned to this category as a new regular verb; it often happens for verbs "borrowed" from 
#     English and for informatical neologisms: chattare, twittare, postare, spammare... will edabittare be the next?

def conjugate(verb, pronoun):
    conjD = {1:["Io","o"], 2:["Tu","i"], 3:["Egli","a"], 4:["Noi","iamo"], 5:["Voi","ate"], 6:["Essi","ano"]}
    verb = verb[:-3]
    verb = verb[:-1] if verb[-1] == "i" and conjD[pronoun][1][0] == "i" else verb
    verb = verb + "h" if verb[-1] == "c" or verb[-1] == "g" else verb
    return conjD[pronoun][0] + " " + verb + conjD[pronoun][1]

"""print(conjugate("programmare", 5)) # ➞ "Voi programmate"
print(conjugate("iniziare", 2)) # ➞ "Tu inizi"
print(conjugate("mancare", 4)) # ➞ "Noi manchiamo"""

print(conjugate("edabittare", 4)) #, "Noi edabittiamo", "We edabit :-)")
print(conjugate("programmare", 5)) #, "Voi programmate", "You code")
print(conjugate("iniziare", 2)) #, "Tu inizi", "You start")
print(conjugate("mancare", 4)) #, "Noi manchiamo", "We miss")
print(conjugate("parlare", 1)) # "Io parlo", "I speak")
print(conjugate("sognare", 3)) #, "Egli sogna", "He dreams")
print(conjugate("negare", 2)) #, "Tu neghi", "You deny")
print(conjugate("insegnare", 5)) #, "Voi insegnate", "You teach")
print(conjugate("tagliare", 4)) #, "Noi tagliamo", "We cut")
print(conjugate("nuotare", 1)) #, "Io nuoto", "I swim")
print(conjugate("cambiare", 3)) #, "Egli cambia", "He changes")

"""def conjugate(verb, pr):
	l = [('Io',	'o'),('Tu','i'),('Egli','a'),
			('Noi', 'iamo'), ('Voi', 'ate'), ('Essi', 'ano')]
	v = verb.replace('are','')
	if v[-1] in 'cg' and pr in[2,4]: v+='h'
	if v[-1] == 'i' and pr in[2,4]: v= v[:-1]
	return l[pr-1][0] + ' ' + v + l[pr-1][1]"""