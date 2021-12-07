import csv

with open('./resource/sample3.csv', 'r') as f:
  reader = csv.reader(f)
  sum = 0
  for c in reader:
    a=int(c[0])
    sum+=a
  print(sum)
