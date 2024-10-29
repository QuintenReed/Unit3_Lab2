# Quinten Reed
# U3L2
# n factorial

def for_factorial(num):
  result = num

  for i in range(num-1, 0, -1):
    result *= i

  return result

def while_factorial(num):
  result = num
  num -= 1

  while num >= 1:
    result *= num
    num -= 1

  return result

def recursion_factorial(num, result):
  if num > 1:
    result = recursion_factorial(num-1, result*(num-1))

  return result

def main():
  num = 4

  for_solve = for_factorial(num)
  while_solve = while_factorial(num)
  recursion_solve = recursion_factorial(num, num)

  print(f"For loop: {for_solve}")
  print(f"While loop: {while_solve}")
  print(f"Recursion: {recursion_solve}")

if __name__ == "__main__":
  main()