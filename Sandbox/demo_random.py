import random
import secrets

# random.seed(983427)

# print( random.randint(1, 100) )

print( [random.randint(1, 100) for _ in range(20)]  )

print( [secrets.randbelow(100) + 1 for _ in range(20)]  )