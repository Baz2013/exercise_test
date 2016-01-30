s = ["a111", "b222", "c333", "d444", "e555"]
s1 = ["a111", "b222", "d444", "e555"]
found = False

for item in s:
    if item.startswith('c'):
        print 'found the word start with the character \'c\''
        found = True
        break

if not found:
    print 'not found the word start with the character \'c\''

print '----------------------------------------------------------------------'

for item in s:
    if item.startswith('c'):
        print 'found the word start with the character \'c\''
        break
else:
    print 'not found the word start with the character \'c\''

