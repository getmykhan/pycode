import numpy as np
from scipy.stats import chisquare
from scipy import stats

s = np.random.uniform(-1,0,1000)
print("**" * int(50))
print(s)
print("**" * int(50))
print(chisquare(s))


n, p = 10, .5  # number of trials, probability of each trial
b = np.random.binomial(n, p, 1000) # result of flipping a coin 10 times, tested 1000 times.
print("**" * int(50))
print(b)
print("**" * int(50))
print(chisquare(b))


p = np.random.poisson(1000, 10)
print("**" * int(50))
print(p)
print("**" * int(50))
print(chisquare(p))
