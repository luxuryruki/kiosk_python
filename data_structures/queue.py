from data_structures.clist import CList

class Queue:
    def __init__(self):
            self.clist = CList()  # CList를 내부적으로 사용
            self.size = 0

    def enqueue(self, value):
        """큐에 요소를 추가"""
        self.clist.add(value)  # CList의 add 메서드를 사용해 맨 끝에 추가
        self.size += 1

    def dequeue(self):
        """큐에서 요소를 제거하고 반환"""
        if self.is_empty():
            print("Dequeue from an empty queue")

        # CList의 첫 번째 노드를 가져오고 제거
        front_value = self.clist.head.value  # head의 값 가져오기
        self.clist.remove(front_value)

        self.size -= 1
        return front_value
    
    def peek(self):
        """큐의 앞쪽 요소를 반환하지만 제거하지 않음"""
        if self.is_empty():
            print("Peek from an empty queue")
        return self.clist.head.value
    
    def is_empty(self):
        """큐가 비어 있는지 확인"""
        return self.size == 0

    def __len__(self):
        """큐의 크기 반환"""
        return self.size