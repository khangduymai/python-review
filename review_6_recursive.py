
#%%

# n! = n.(n-1).(n-2)....3.2.1
# 1! = 1
# 0! = 1

# n! = n.(n-1)!

def fact(n):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

for i in range(10):
    print(i, fact(i))


# %%

# F(n) = F(n-1) + F(n-2)

# F(n) = F(n-1) + F(n-2) if n >=3 
# else 1 (if n = 1 or 2)

def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1


        