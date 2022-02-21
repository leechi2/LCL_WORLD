import sys

input = sys.stdin.readline

txt_list = list(input().rstrip())

data_base = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

count = 0

for i in txt_list:

    for j in data_base:
        if i in j:
            count +=data_base.index(j)+3

print(count)