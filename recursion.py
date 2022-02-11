def factorial(n):
    """Calculate the factorial of 'n' number."""
    # Base case: Condition when this recursive function should stop execution. We know 1!=1 so that's our base case
    if n == 1:
        return 1
    return n*factorial(n-1)
 
print(factorial(10))

# 8!= 8*7*6*5*4*3*2*1 = 8*7!

# 8*7!
# 7*6!
# 6*5!
# 5*4!
# 4*3!
# 3*2!
# 2*1!=2
# 1!=1

def fibonacci(n):
    """Calculate nth number in the fibonacci sequence."""
    # Base case:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(4))
0, 1, 1 , 2, 3, 5