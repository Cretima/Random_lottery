
def made_list1(): # 리스트 제작
    i = 1
    lst1 = []

    lott = int(input("1번부터 몇번까지 추첨할까요?(숫자입력): "))
    
    while i < (lott + 1) :
        lst1.append(i)
        i += 1
    return lst1

def func1(a): # 만들어진 a리스트를 랜덤으로 n번 추첨 
    lst1 = []
    lst1 = a

    number = int(input("그 중 몇개(명)를 추첨할까요? : "))
    
    shuffle(lst1)
    result = sample(lst1, number)
    result.sort() # 뽑힌 수 정렬
    print(f'당첨 결과: "{result}\"')
 
def made_list2(): # 1과 다르게 사용자가 리스트 추가 가능
    lst2 = []
    while True :
        index = input("추첨에 넣고싶은 사람/숫자 등을 입력(그만 입력할려면 end 입력): ")
        if (index == "end") | (index == "End") | (index == "END") :
            break
        else:
            lst2.append(index)
       # break if (index == "end") | (index == "End") | (index == "END") else lst2.append(index)
    return lst2


# main

from random import *

want = input('1~X 사이의 추첨이면 \"1\" 사용자가 원하는대로 입력하는 추첨이면 \"2\"를 눌러주세여: ')
if (want == 1) :
    lst = made_list1()
    func1(lst)
elif (want == 2) :
    lst = made_list2()
    func1(lst)
else:
    print("오류 다시 실행하세요.")
