import random
import math
import sys

"""calculation of all possible examples for a magic square 3x3 in which all columns, rows and diagonals multiply the same, being 15 the central value"""
sq=[[1,1,1],[1,1,1],[1,1,1]]
for k in range(10000000):
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                e3=1.
                e5=1.
            else:
                e3=int(3.*random.random())
                e5=int(3.*random.random())
            sq[i][j]=int(math.pow(3.,e3)*math.pow(5.,e5))
    f1=sq[0][0]*sq[0][1]*sq[0][2]
    f2=sq[1][0]*sq[1][1]*sq[1][2]
    f3=sq[2][0]*sq[2][1]*sq[2][2]
    c1=sq[0][0]*sq[1][0]*sq[2][0]
    c2=sq[0][1]*sq[1][1]*sq[2][1]
    c3=sq[0][2]*sq[1][2]*sq[2][2]
    d1=sq[0][0]*sq[1][1]*sq[2][2]
    d2=sq[0][2]*sq[1][1]*sq[2][0]
    #if k%100000==0: print "executing k=",k,sq
    #print "testing sq",sq
    if f1==f2==f3==c1==c2==c3==d1==d2: 
        print "bingo", sq,f1,f2,f3,c1,c2,c3,d1,d2
     #   sys.exit()

print "program finnished"
