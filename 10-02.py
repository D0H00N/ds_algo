## 함수
def openbox() :
    global count
    print('상자를 열자')
    count -= 1
    if count == 0 :
        print('선물을 넣자')
        return
    openbox()
    print('상자를 닫자')
    return

## 메인
count = 10
openbox()