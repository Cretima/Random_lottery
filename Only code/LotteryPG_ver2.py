# 22 - 01 - 16
from encodings import utf_8_sig
import string
import csv
from random import *

def made_list1(): # 리스트 제작
    lott = int(input("1번부터 몇번까지 추첨할까요?(숫자입력): "))
    list1 = range(1, lott + 1) # 1 ~ 21 직전까지 생성. step 1 씩
    list1 = list(list1)
    return list1

def func1(a): # 만들어진 a리스트를 랜덤으로 n번 추첨 
    lst1 = a

    number = int(input("그 중 몇개(명)를 추첨할까요? : "))
    
    shuffle(lst1)
    result = sample(lst1, number)
    result.sort() # 뽑힌 수 정렬
    print(f'당첨 결과: \"{result}\"')
 
def made_list2(): # 1과 다르게 사용자가 리스트 추가 가능
    data1 = input("추첨에 넣고싶은 사람/숫자 등을 입력(그만 입력할려면 end 입력): ").split(" ")
    # .split() 괄호안의 문자로 문자열을 구분해서 리스트로 만들어줌
    # "No Thank Kim".split(" ") >> ["No", "Thank", "Kim"]

    f = open("data_list.csv", "w", encoding="utf_8_sig", newline = "") # newline="" writerow후에 다음행으로
    csv.writer(f).writerow(data1)
    f.close()

def func2():
    f = open("data_list.csv", "r", encoding="utf_8_sig")
    reader = csv.reader(f)
    
    data2 = list(reader)

    number = int(input("그 중 몇개(명)를 추첨할까요? : "))
    
    shuffle(data2[0]) # data2[0] >> 2차원 배열을 0행을 추출.
    result = sample(data2[0], number) # 1차원 배열일때만 적용.
    result.sort() # 뽑힌 수 정렬
    print(f'당첨 결과: \"{result}\"')


# main

want = int(input('1~X 사이의 추첨이면 \"1\" 사용자가 원하는대로 입력하는 추첨이면 \"2\"를 눌러주세여: '))
if (want == 1) :
    func1(made_list1())
elif (want == 2) :
    made_list2()
    func2()
else:
    print("오류 다시 실행하세요.")