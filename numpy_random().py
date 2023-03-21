
import numpy as np
from numpy.random import random
random()

ans = None
x = random()
if x > 0.5 :
  ans = "greater"
else:
  if x > 0.3 :
    ans = "small"
  else:
    ans = "hey!!"
print(x)
print(ans)
