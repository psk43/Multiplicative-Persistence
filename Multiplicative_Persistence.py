#The persistence of a number
#is the number of times you need to multiply the digits together
#before reaching a single digit

from functools import reduce
import time

persistence = 0
result = 11
initTime = 0

def productFinder(number):
    global result
    operands = [int(i) for i in str(number)]
    result = reduce(lambda x,y: x*y, operands)
    #result = int(''.join(str(i) for i in result))
    print('stage %d result: %d' %(persistence,result))
    #print('Time taken for stage %d : %s seconds' % (persistence,(time.time()-initTime)))

def main():
    global result
    global persistence
    inp = input('Enter the number --->  ')
    initTime = time.time()
    inp = int(inp)
    result = inp
    while(result>10):
        persistence = persistence + 1
        productFinder(result)
    print('\nMultiplicative persistence of %d is: %d' %(inp,persistence))

if __name__ == '__main__':
  main()
