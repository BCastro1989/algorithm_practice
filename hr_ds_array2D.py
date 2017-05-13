
import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

sums = []
for y in xrange(0,len(arr)-2):
    for x in xrange(0,len(arr[y])-2):
        hg_sum  = sum(arr[y][x:x+3])
        hg_sum += arr[y+1][x+1]
        hg_sum += sum(arr[y+2][x:x+3])
        #print arr[y][x:x+2]
        #print arr[y+1][x+1]
        #print arr[y+2][x:x+2]
        sums.append(hg_sum)
        #print (x, y), "|", hg_sum

#print sums
print max(sums)
        
