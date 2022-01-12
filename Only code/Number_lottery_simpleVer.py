def made_list(a): # 리스트 제작
    n = 1
    lst = []
    while n < (a + 1) :
        lst.append(n)
        n += 1
    return lst

def func1(a, n): # 만들어진 a리스트를 랜덤으로 n번 추첨 
    lst = []
    lst = a
    shuffle(lst)
    result = sample(lst, n)
    result.sort() # 뽑힌 수 정렬
    print(f'추첨된 숫자는?: \"{result}\"')

from random import *
lott = int(input("1번부터 몇번까지 추첨할까요?(숫자입력): "))
number = int(input("그 중 몇개를 추첨할까요?(중복 추첨 불가): "))
lst = made_list(lott)
#print(lst)
func1(lst, number)