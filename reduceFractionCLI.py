import sys

def gcd(a,b):
    toReturn = 1
    for num in range(min(a,b)):
        if a%(num+1) == 0 and b%(num+1) == 0:
            toReturn = num+1
    return toReturn

def reduceFraction(a,b):
    common = gcd(a,b)
    return a//common, b//common

def main():
    if len(sys.argv) < 2 or sys.argv[1].count('/') != 1:
        print('Requires argument in the form of int1/int2 where num1 and num2 are both integers')
    else:
        numStrList = sys.argv[1].split('/')
        areInts = True
        for numStr in numStrList:
            if not numStr.isnumeric():
                areInts = False
        if areInts:
            result = reduceFraction(int(numStrList[0]),int(numStrList[1]))
            print(f'{result[0]}/{result[1]}')
        else:
            print('int1 and/or int2 cannot be identified as integers')

main()

