def nest_list_sum(li):
    li = str(li).replace(" ","")
    nestedsum = 0
    nest = 0
    i = -1
    #for each char in list-as-str
    while True:
        #advance index and break if invalid
        i += 1
        if i >= len(li):
            break
        #get char and check for non-ints
        c = li[i]
        if c == "[": #change nest level
            nest += 1
            continue
        if c == "]": #change nest level
            nest -= 1
            continue
        if c == ",":
            continue
        num = ""

        #if number found (assumes always given valid list of int)
        while True:
            if li[i] == "]": #end number and add to sum
                nestedsum += int(num)*nest
                nest -= 1
                break
            if li[i] == ",": #end number and add to sum
                nestedsum += int(num)*nest
                break
            #add char to number (multi-digit)
            num += li[i]
            i += 1

    return nestedsum

li1 = [[1,3,4],[3,2,[23,0,9]],[2,9],9,9,1]
ans = nest_list_sum(li1)
print "SUM:", ans

li2 = [1, [2, 3]]
ans = nest_list_sum(li2)
print "SUM:", ans

li3 = [1, [2, [3]]]
ans = nest_list_sum(li3)
print "SUM:", ans




################################################
#Better/Neater Implemntation
###############################################
def nested_list_sum(nlist, depth=1):

    weighted_sum = 0;

    for n in nlist:
      #if int, add it
      if type(n) is int:
        print "B", n, "*", depth, "=", n*depth
        weighted_sum += n*depth
      #else, call function again, add depth
      else:
        weighted_sum += nested_list_sum(n,depth+1)

    return weighted_sum



d = [1,[4,[6]]]
print nested_list_sum(d)

d = [[[[1],2],3],12,3,1,[4,[6]]]
print nested_list_sum(d)

d = [1,2,3]
print nested_list_sum(d)

d = [[[[[1]],2]],2,3,[3],[[1]],[1,2,3],[6,[4,3,2]]]
print nested_list_sum(d)

d = [[[[[[[[[[1,2,3]]]]]]]]]]
print nested_list_sum(d)

    #originally in soln but seems unnessecary...
    
    # #if root is int, add it to sum
    # if type(root) is int:
    #   print "A", n, "*", depth, "=", n*depth
    #   weighted_sum += root*depth
    # #else it's a list
    # else:
    # nlist = root
    #for element in list
