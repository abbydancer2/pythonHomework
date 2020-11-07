""" spells.py  This program takes a list of spells, and a list of occurances and
    replaces the spells list with spell casts based on the count in occurances, with !!!
    added.  It does this by first using a standard loop to build the new list and then uses
    a mapped lambda function to rebuild the list """


spells = ["protego", "accio", "expecto patronum", "legilimes"]
counted_spells = []
occurance = [1, 0, 2, 1]
for index in range(0, len(occurance)):
    for number in range(0, occurance[index]):
        counted_spells.append(spells[index])
spells = list(map(lambda s: s + "!!!", counted_spells))
print(spells)
