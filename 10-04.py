5288893@hanafos.com 특강 강사님 메일

## 함수
def factorial(num) :
    if num <= 1  :
        print('1반환')
        return 1
    print("%d * %d! 호출" % (num,num-1))
    retVal =factorial(num-1)

    print("%d * %d!(=%d) 반환" % (num,num-1,retVal))
## 메인

print('\n5!', factorial(5))
return num * retVal