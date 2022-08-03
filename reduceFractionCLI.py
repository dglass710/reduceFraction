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
        print('Requires argument in the form of \033[91mint1/int2\033[0m where \033[93mint1\033[0m and \033[93mint2\033[0m are both integers')
    else:
        numStrList = sys.argv[1].split('/')
        areInts = True
        for numStr in numStrList:
            if not numStr.isnumeric():
                areInts = False
        if areInts:
            result = reduceFraction(int(numStrList[0]),int(numStrList[1]))
            print(f'\033[96m{numStrList[0]}/{numStrList[1]}\033[0m = \033[95m{result[0]}/{result[1]}')
        else:
            print('\033[93mint1\033[0m and/or \033[93mint2\033[0m cannot be identified as integers')

main()

