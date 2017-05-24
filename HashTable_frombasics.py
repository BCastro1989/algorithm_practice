class HashTable():
    def __init__(self,size):
        self.size = size
        self.ht = [ [] for x in xrange(0,size)]

    def str2int(self,key):
        '''Convert string to sum of ascii values'''
        total = 0
        for c in key:
            total += ord(c)
        return total

    def hash_it(self,key):
        '''simple hash function: mod key by ht size to get index'''
        if type(key) == str:
            key = self.str2int(key)
        return key%self.size

    def add(self,key,val):
        ''' Add a new key and valye to ht'''
        hsh = self.hash_it(key)
        self.ht[hsh].append((key,val))

    def del_key(self,key):
        ''' delete all entries associated with a key'''
        del self.ht[self.hash_it(key)]

    def lookup_key(self,key):
        ''' Give list of elements for that key '''
        try:
            return self.ht[self.hash_it(key)]
        except:
            print "No such key"

ht_example = HashTable(5)

print "Initialize"
print ht_example.ht
print "Added key/val pairs"
ht_example.add(12,9)
ht_example.add(34,14)
ht_example.add(955,44)
ht_example.add(2,53)
ht_example.add("Bob",25)
ht_example.add("Sue",27)
ht_example.add("John",64)
ht_example.add("Paul",66)
ht_example.add("George",74)
ht_example.add("Ringo",70)
print ht_example.ht
print "lookup by key"
print ht_example.lookup_key("Sue")
