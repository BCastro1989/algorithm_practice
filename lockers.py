#There are n (n >=1) students, who line up in a room with n lockers (labelled with 1, 2, ..., n) that are all closed.
#  - The 1st student opens all lockers;
#  - The 2nd student TOGGLES (open -> closed or closed -> open) every other locker, starting from the 2nd locker, that means, after the 2nd student, lockers 2, 4, 6, 8.. will be closed;
#  - The 3rd student TOGGLES the 3rd, 6th, 9th...;
#  - The 4th student TOGGLES the 4th, 8th, 12th....;
#  - Until the n-th student finishes.
#Print out all the lockers that are open when the last ##(n-th) student finishes.

#n students
#n lockers
#1 switches every
#2 switches every 2nd
#3 switches every 3rd...

#START CLOSED
#1 = open
#0 = closed

def locker_open_closed(n):
    lockers = [0]*n

    #for each student
    for i in xrange(0,n):

        #for each locker
        for l in xrange(0,n,i):
            lockers[l] = (lockers[l]+1)%2

    for i in lockers:
        if lockers[i] == 1:
            print i


    
