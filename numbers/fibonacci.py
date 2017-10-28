'''
generate the fibonacci sequence up to the nth digit
@author: Russ Winch
@version: Oct 2017
'''

def fibonacci(n):
    a = 1
    b = 0
    for i in range(int(n)):
       f = a+b
       print(f) 
       a = b
       b = f

def fibonacci2(n):
    try:
        n = int(n)
    except ValueError:
        print('enter a number!')
        return
    fibo = [0,1]
    for i in range(2,n):
       fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[0:n]

fibs = input('how many digits? : ')
# fibonacci(fibs)
print(fibonacci2(fibs))
