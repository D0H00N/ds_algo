## 함수
import random
def binSearch(ary, fdata) :
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        middle = (start+end) // 2
        if (ary[middle] == fdata) :
            pos = middle
            break
        elif (ary[middle] < fdata) :
            start = middle + 1
        else :
            end = middle - 1
    return pos






    return pos
## 변수
dataAry = [random.randint(30, 190) for _ in range(10)]
findData = random.choice(dataAry) # 할머니 키
dataAry.sort()

## 메인
print('배열->', dataAry)
position = binSearch(dataAry, findData)
if (position != -1) :
    print(findData,'는', position, '에 위치')
else :
    print(findData,'는 없다')

    