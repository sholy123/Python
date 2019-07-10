
def isPrime(num):
    i = 2
    if num == 2 or num == 3:
        return True
    while i <= (num/2):
        if num % i == 0:
            return False
        i = i+1
    return True

def isDaffodil(num):
    res = 0
    num2 = num
    a = []
    while num != 0:
        yu = num % 10
        num = int(num / 10)
        a.append(yu)
    for i in a:
        res = res + i**3
    if res == num2:
        return True
    else:
        return False
if __name__=="__main__":
    isDaffodil(153)
    for r in range(100,1000):
        if isDaffodil(r):
            print("this is:",r)
    for i in range(2,100):
        if isPrime(i):
            print(i)


