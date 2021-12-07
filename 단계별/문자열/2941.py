import sys

input = sys.stdin.readline

txt_list = list(input().rstrip())
count = len(txt_list)

for i in range(len(txt_list)):

    if txt_list[i] == '=':
        count-=1
        if i > 0:
            if txt_list[i-1] == 'z' and txt_list[i-2] == 'd' :
                count -=1
    if txt_list[i] == '-':
        count -=1
    if txt_list[i] == 'j':
        if i > 0:
            if txt_list[i-1] == 'l':
                count -=1
            elif txt_list[i-1] == 'n':
                count -=1
        
print(count)