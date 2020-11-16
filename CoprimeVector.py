import random
import sys

def main():

    amount = 1000000
    min = 0
    max = sys.maxsize #To get some big integer

    #Fixed Length from 2 to 6
    for i in range(2,7):
        result = 0
        #Generate N amount of array with fixed length above
        for a in range(amount):
            array = []
            for l in range(i):
                array.append(random.randint(min, max))
            resultGCD = gcd(array)
            #Calculator percentage of set-wise vectors
            if resultGCD == 1:
                result += 1
        percentage = round(result/amount*100, 2)
        print(f"The percentage of set-wise coprime vectors among {amount} vectors with fixed length = {i} and range = [{min},{max}) is equal to {percentage}%")

#Function to calculate gcd of arrays with 2 and more elements
def gcd(array):
    num1 = array[0]
    num2 = array[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(array)):
        gcd = find_gcd(gcd, array[i])

    return gcd

def find_gcd(a,b):
    if(b==0):
        return a
    else:
        return find_gcd(b,a%b)

if __name__ == '__main__':
    main()