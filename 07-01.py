## 함수


## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인

## enQueue()
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구-->', queue, '<--입구')

## deQueue()
front += 1
reData = queue[front]
queue[front] = None
print('손님 이리로 : ', reData)


front += 1
reData = queue[front]
queue[front] = None
print('손님 이리로 : ', reData)

front += 1
reData = queue[front]
queue[front] = None
print('손님 이리로 : ', reData)

print('출구-->', queue, '<--입구')