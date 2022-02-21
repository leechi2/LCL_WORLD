import sys
input = sys.stdin.readline 

def jg(list):
    st = []
    for i in range(len(list)):
        if list[i] == '(':
            st.append(0)
        elif list[i] == ')':
            if len(st) == 0:
                return False
            else:
                if st[-1] == 0:
                    st.pop()
                else:
                    return False
        elif list[i] == '[':
            st.append(1)
        elif list[i] == ']':
            if len(st) == 0:
                return False
            else:
                if st[-1] == 1:
                    st.pop()
                else:
                    return False
        else:
            continue
    if st == []:
        return True


temp = []
while temp != ['.']:
    temp = list(input().rstrip())
    if temp == ['.']:
        break
    elif jg(temp) == True:
        print('yes')
    else:
        print('no')