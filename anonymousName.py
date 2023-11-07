"""You are in the process of creating a chat application and want to add an anonymous name feature. This anonymous name feature will 
create an alias that consists of two capitalized words beginning with the same letter as the users first name.

Create a function that determines if the list of users is mapped to a list of anonymous names correctly.
Examples

is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]) ➞ True

is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"]) ➞ True

is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]) ➞ False
# Both words in "Brandishing Mimosa" should begin with a "B" - "Brandishing Beaver" would do the trick.

Notes

Both words in the alias should be capitalized."""
def is_correct_aliases(names, aliases):
    return all(i[0][0]==i[1][0][0] and i[0][0]==i[1][1][0] for i in zip(names, map(lambda x: x.split(), aliases)))

print(is_correct_aliases(['Adrian M.', 'Harriet S.', 'Mandy T.'], ['Amazing Artichoke', 'Hopeful Hedgehog', 'Marvelous Mouse'])) #, True)
print(is_correct_aliases(['Rachel F.', 'Pam G.', 'Fred Z.', 'Nancy K.'], ['Reassuring Rat', 'Peaceful Panda', 'Fantastic Frog', 'Notable Nickel'])) #, True)
print(is_correct_aliases(['Beth T.'], ['Brandishing Mimosa'])) #, False)
print(is_correct_aliases(['Mick S.', 'Sam R.', 'Val W.'], ['Magnificent Mint', 'Sly Serpent', 'Victorious Viceroy'])) #, True)
print(is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Cool Bamboo'])) #, False)
print(is_correct_aliases(['Bella T.', 'Tom H.', 'Ben C.'], ['Beautiful Barn', 'Talented Tapestry', 'Bountiful Bamboo'])) #, True)

"""def is_correct_aliases(names, aliases):
	return all(i[0] == j.split()[0][0] == j.split()[1][0] for i, j in zip(names, aliases))"""