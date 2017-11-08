import numpy as np
import random
from math import sqrt

def MSV(*args):
	l = list(args[0])
	print(l)
	Mean = sum(l) / len(l)
	
	sd = 0
	for i in l:
		sd = sd + ((i - Mean)**2)
	sd = sqrt(sd / len(l))

	vr = sd **2
	print("Mean of the chosen List:", Mean)
	print("SD of the chosen List:", sd)	
	print("Variance of the chosen List:", vr)



MSV(np.random.randint(0, 100, random.randint(1,11)))
