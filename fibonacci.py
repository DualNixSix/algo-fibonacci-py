def fibonacci(n):
  if n == 0:  # 0 returns 0
    return 0
  elif n == 1 or n == 2: # 1 or 2 returns 1 
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2) # use the formula F(n) = F(n-1) + F(n-2)
pass


