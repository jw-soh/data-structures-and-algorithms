# Problem: Print numbers from 1 to 10 recursively
# observation:
# printing 1 to 10 can be divided into smaller versions of the same problem
# e.g.
# printing 1 to 10 is the same as printing 1 then printing 2 to 10 (Print numbers from 2 to 10 recursively).
# printing 2 to 10 is the same as printing 2 then printing 3 to 10 (Print numbers from 3 to 10 recursively).

def printUpToTen(n):
  if n > 10:
    return
  print(n) # executing the bitesize chunk of the divided problem
  printUpToTen(n + 1) # the remaining larger chunk of the divided problem

printUpToTen(1)