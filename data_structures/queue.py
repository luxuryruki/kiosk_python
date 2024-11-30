from data_structures.clist import CList

class Queue:
    def __init__(self):
            self.clist = CList() 
            self.size = 0

    def enqueue(self, value):
        """큐에 요소를 추가"""
        self.clist.add(value)  
        self.size += 1

    def dequeue(self):
        """큐에서 요소를 제거하고 반환"""
        if self.is_empty():
            print("Dequeue from an empty queue")

        front_value = self.clist.head.value 
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