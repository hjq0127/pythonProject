"""
 What did you see on line 1?
 7
 What was the smallest number you could have seen, what was the largest?
 Smallest is 5, largest is 20
 What did you see on line 2?
 3
 What was the smallest number you could have seen, what was the largest?
 Smallest is 3, largest is 9
 Could line 2 have produced a 4?
 Cannot
 What did you see on line 3?
 3.8856197973174544
 What was the smallest number you could have seen, what was the largest?
 Smallest is 2.5, largest is 5.5
"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.randint(1, 100))