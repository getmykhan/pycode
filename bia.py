import numpy as np
from scipy.stats import chisquare
from scipy import stats


s = np.random.uniform(low=0.5, high=13.3, size=(1000,))
print("**" * int(50))
print(s)
print("**" * int(50))
print(chisquare(s))


n, p = 10, 0.7  # number of trials, probability of each trial
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

b_norm = np.random.standard_normal((1000,))
print(stats.kstest(b_norm, 'norm'))
