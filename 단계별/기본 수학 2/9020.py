import sys

input = sys.stdin.readline

number = int(input())

def prime(n):
  temp = False
  for i in range(2,int(n**(1/2))+1):
    if n % i == 0:
      temp = True
      break
  return temp

for _ in range(number):
  p = int(input())
  for i in range(p//2,1,-1):
    if not prime(i):
      if not prime(p-i):
        print(i, p-i)
        break