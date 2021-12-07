# section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv 콤마로 구분된다고 'C'SV

import csv

# ex1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) 맨 처음에 1 행을 스킵할때
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

print('___________________-')
# ex1
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|')
    # 특정 구분자 일때 delimiter = '특정 문자'
    # next(reader) 맨 처음에 1 행을 스킵할때
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    for c in reader:
        print(c)

# ex3 (Dict 변환)

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('---------')

# ex4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w', newline="") as f:
    # newline="" 엔터가 두번되가지고 open 에서는 엔터 안되도록
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# ex5

with open('./resource/sample4.csv','w', newline="") as f:
    # newline="" 엔터가 두번되가지고 open 에서는 엔터 안되도록
    wt = csv.writer(f)
    wt.writerows(w) # for 문 없이 한방에 쓰기

# XSL, XLSX 읽기
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 엑셀을 처리하는 오픈소스
# 다양한 오픈 소스 중 pandas 를 주로 사용
# 왜냐하면 pandas안에 1,2등인 openpyxl, xlrd 가 내부에 있음

import pandas as pd
xlsx = pd.read_excel('./resource/sample.xlsx', header=5)
# sheetname='시트명' 또는 숫자, header = 숫자, skiprow= 숫자
# 상위 데이터 확인
print(xlsx.head()) # head는 처음부터 5개만 보여줌
print()
print(xlsx.tail())
print()
print(xlsx.shape) # 행, 열 을 보여준다

# 엑셀 or cvs 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)