#NOTE:
#
# I you are reading this it is because I had to end my internet session and 
# I was unable to get this to load again when I returnted to my computer
#
# So this is how far I got with 2 hr 21 min remaining. Hopefully though once
# I am able to log back on I will be able to start where I left off
# with time elapse of course, but I hope I will at least not loose my work
# or be unable to rejoin this test



# Complete the function below.
def lovedNums(bounds):
    #very crappy method
    #go through range, add to counter whenever theres no repeated digits
    #lo, hi = bounds[0], bounds[1]
    #for n in xrange(lo,hi+1):
    #    for c in str(n):
    #        for d in str(n):
                #Polynomial Time... yeah no... scratch that
        
    #better method
    lo, hi = bounds[0], bounds[1]
    # n * n log(m) time... still not great (m here is digits in a number)
    loved_count = 0
    for n in xrange(lo,hi+1):
        #turn to str and sort digits
        num_sorted_digits = sorted([c for c in str(n)])
        #if any digit is = to digit next, incriment counter
        #print num_sorted_digits
        for i in xrange(1,len(num_sorted_digits)):
            if num_sorted_digits[i] == num_sorted_digits[i-1]:
                #print "match! no increment"
                break
        #no repeats, increment counter
        loved_count += 1
                
           
    return loved_count - 1 
    
    #best method
    #there exists a mathematical relationship that will tells us this for any arbitary range. Find it.
    
    #for range 0-9, 9 digits w/ NO repeats; (9)
    #for range 10-99, 89 digits w/ NO repeats (9*9 = 89)
    #for range 100-999, 648 digits w/ NO repeats (9*9*8 = 648)
    #for range 1000-9999, 4536 digits w/ NO repeats (9*9*8*7 = 4536)
    #...
    #for range 100000000-99999999, 3265920 digits w/ NO repeats (9*9*8*7...*1 = 3265920)
    #for range 1000000000-999999999, and above, NO digits with no repeats
    #But how to get this for arbitary range? hmm...
    

def  countNumbers(arr):
    soln = []
    for bounds in arr:
        soln.append(lovedNums(bounds))

    for elem in soln:
        print elem

