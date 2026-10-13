def bisection_root(x, epsilon=0.01):
    low = 0
    high = x
    guess = (high + low) / 2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

print(bisection_root(123))


