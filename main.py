# Author: Dominic Savaglio djs7129@psu.edu
def digit_sum(n):
  if n == 0:
    return 0
  else:
    return n % 10 + digit_sum(n // 10)
def run():
  sum = int(input("Enter an int: "))
  digit_sum(sum)
  print(f"sum of digits is {digit_sum(sum)}.")
if __name__ == "__main__":
  run()