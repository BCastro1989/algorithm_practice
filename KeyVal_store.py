
# 1. Build a key/value (KV) store with transactions

# KV store has following operations:

# Operations:

# add( K key, V value) : void , maps the key to the value, if key already present replaces with the current value
# getValue(key) : V, returns the value attached to the key
# getKey(v value) K[], return all the keys which is associated with the given value
# delete(key): void, delete the key if present, else do nothing
# begin(): void, begin a transaction
# rollback(): void, rollback the previous updates from the recent begin() statement
# commit(): void, commit the current changes to the kvStore

# Constraints: Operations add, getValue, delete, getKey should be constant time
# Example operations:



# add - add new dictionay K,V

# getValue - get value for key in dict

# get Key - get keys that have value

# delete - delete the key

# begin - store a dict, dont make instant modifications

# rollback - call stored dict

# commit - changes take effect

import copy

class KVstore():

    def __init__(self):
        self.KVdict = {}
        self.KVstored = {}
        self.KV_getKey = {}

    def add(self,key,val):
        self.KVdict[key] = val

        #modify later to take into account for overwriting
        if val in self.KV_getKey:
            self.KV_getKey[val].append(key)
        else:
            self.KV_getKey[val] = [key]

    def getValue(self,key):
        return self.KVdict[key]

    def getKey(self,val):
        return self.KV_getKey[val]

    def delete(self,key):
        self.KVdict.pop(key)#none

    def begin(self):
        self.KVstored = copy.deepcopy(self.KVdict)

    def rollback(self):
        self.KVdict.clear
        self.KVdict = copy.deepcopy(self.KVstored)

    def commit(self):
        self.KVstored.clear
        #self.KVdict = copy.deepcopy(self.KVstored)


kvs = KVstore()
kvs.add("A",2)
kvs.add("B",2)
kvs.add("C",8)
kvs.add("D",4)
print kvs.getValue("A")

print kvs.getKey(2)

kvs.delete("B")

print kvs.getKey(2)

kvs.begin()
kvs.add("F",21)
kvs.add("G",22)
kvs.add("A",821)
kvs.add("H",24)

print kvs.getValue("A")
kvs.rollback()
print kvs.getValue("A")


# 1)

# kvStore .add(k1, v1)
# Current KV Object State:
# {k1: v1}

# 2)

# kvStore .add(k2, v2)
# Current KV Object State:
# {
#   k1:v1
#   k2:v2
# }

# 3)

# kvStore .begin()
# kvStore .add(k1, v3)
# Current KV Object State:
# {k1:v3
#  k2:v2
# }

# 4)
# kvStore .add(k1, v4)
# Current KV Object State:
# {k1: v4
#  k2: v2}

# 5)
# kvStore .rollback()
# Current KV Object State:
# {k1:v3
#  k2:v2
#  }

# 6)
# kvStore .commit()
# Current KV Object State:
# {k1:v3
#   k2:v2}

# 7)
# kvStore.rollback() - No operation , has effect only within a transaction
# Current KV Object State:
# {k1: v3
#  k2: v2}

# 8)
# kvStore .begin()
# kvStore .add(k3, v3)

# Current KV Object State:
# {k1:v3
#   k2:v2
#   k3:v3
#  }

# 9)
# kvStore .rollback()
# Current KV Object State:
# {
#  k1:v3
#  k2:v2
# }

# 10)
# kvStore .commit()
# Current KV Object State:
# {k1: v3
#  k2: v2}
