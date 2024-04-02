name = input('Enter file:')
handle = open(name, 'r')
counts = dict()
a = 10
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

#bigcount = None
#bigword = None
#print(list(counts.items()))
#for word, count in list(counts.items()):
    #print("word", word)
    #print("bigcount", bigcount)
    #print("count", count)
    #if bigcount is None or count > bigcount:
        #bigword = word
        #bigcount = count
        #print("inside loop" , bigword, bigcount)
#print(bigword, bigcount)