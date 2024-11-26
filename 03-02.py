## 함수
# 데이터 추가 함수
def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    # 2단계 : 배열의 길이를 파악
    KLen = len(katok)
    # 2단계 : 마지막 칸에 친구 넣기
    katok[KLen-1] = friend
# 데이터 삽입 함수
def insert_data(position, friend) : #3, 미나
    # 1단계 : 빈칸 추가
    katok.append(None)
    KLen = len(katok)
    # 2단계 : 반복문 처리
    for i in range(KLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 미나를 넣기
    katok[position] = friend
# 데이터 삭제 함수
def delete_data(position) : #
    # 1단계 : 그 위치 주이기
    katok[position] = None
    KLen = len(katok)
    # 2단계 : 지운 위치 다음부터, 마지막 친구까지 한 칸씩 앞으로
    for i in range(position+1, KLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None
        # 3단계 : 마지막 칸을 완전 제거
    del(katok[KLen-1])

## 전역
katok = []
select = -1

## 메인

while (select !=4) :
    select = int(input("선택하세요(1:추가,2:삽입,3:삭제,4:종료)-->"))

    if (select == 1) :
        data = input("추가할 데이터-->")
        add_data(data)
        print(katok)
    elif(select == 2) :
        pos = int(input("삽입할 위치-->"))
        data = input("추가할 데이터-->")
        insert_data(pos, data)
        print(katok)
    elif (select == 3) :
        pos = int(input("삭제할 위치-->"))
        delete_data(pos)
        print(katok)
    elif (select == 4) :
        print(katok)
        exit()
    else :
        print("1~4 중 하나를 입력하세요.")
        continue

# add_data('다현')
# add_data('정연')
# add_data('쯔위')
# add_data('사나')
# add_data('지효')
# print(katok)
# add_data('모모')
# print(katok)
#
# insert_data(3, '미나')
# print(katok)
#
# delete_data(4)
# print(katok)