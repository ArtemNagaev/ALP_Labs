import sys
sys.setrecursionlimit(10000)
def ackerman(m, n):
    if m==0:
        return n+1
    elif m==1:
        return n+2
    elif m>0 and n==0:
        return ackerman(m-1, 1)
    elif m>0 and n>0:
        return ackerman(m-1, ackerman(m, n-1))

print(ackerman(0,0))
print(ackerman(0,1))
print(ackerman(0,2))
print(ackerman(0,3))
print(ackerman(0,4))
print(ackerman(0,5))
print(ackerman(1,0))
print(ackerman(2,0))
print(ackerman(3,0))
print(ackerman(4,0))
print(ackerman(3,5))
