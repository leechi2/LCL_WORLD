import sys

input = sys.stdin.readline

a,b,c= map(int, input().split())


def right_triangle(a,b,c):
  if a**2 == b**2 + c**2:
    print('right')
  else:
    print('wrong')
    
while (a,b,c) != (0,0,0):
  
  if c == max(a,b,c):
    right_triangle(c,a,b)
  elif b == max(a,b,c):
    right_triangle(b,a,c)
  else:
    right_triangle(a,b,c)
  a,b,c= map(int, input().split())