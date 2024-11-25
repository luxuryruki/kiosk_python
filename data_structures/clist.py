class CNode:
    def __init__(self, value=None,  prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return f"CNode(value={self.value})"
 

class CList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        """리스트 끝에 값을 추가"""
        new_node = CNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.next_node = self.head  # 원형 연결
            self.head.prev_node = self.head
        else:
            new_node.prev_node = self.tail
            new_node.next_node = self.head

            self.tail.next_node = new_node
            self.head.prev_node = new_node
            self.tail = new_node
        print(f"CList_Added: {value}")

    def read(self, value):
        """값에 해당하는 노드를 반환"""
        if not self.head:
            return None

        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next_node
            if current == self.head:  # 한 바퀴 돌면 검색 종료
                break

        return None 

    def remove(self, value):
        """리스트에서 특정 값을 가진 노드를 삭제"""
        if not self.head:
            print("CList is empty. Nothing to remove.")
            return

        current = self.head
        while True:
            if current.value == value:
                # 노드 삭제
                if current == self.head and current == self.tail:
                    # 리스트에 노드가 한 개만 있는 경우
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    # 삭제할 노드가 head인 경우
                    self.head = self.head.next_node
                    self.head.prev_node = self.tail
                    self.tail.next_node = self.head
                elif current == self.tail:
                    # 삭제할 노드가 tail인 경우
                    self.tail = self.tail.prev_node
                    self.tail.next_node = self.head
                    self.head.prev_node = self.tail
                else:
                    # 중간 노드 삭제
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                print(f"CList_Removed: {value}")
                return
            current = current.next_node
            if current == self.head:
                # 리스트를 한 바퀴 돌았는데 값이 없음
                break
        print(f"Value {value} not found in the list.")

    def display(self):
            """리스트의 모든 값을 출력"""
            if not self.head:
                print("CList is empty")
                return

            current = self.head
            values = []
            while True:
                values.append(current.value)
                current = current.next_node
                if current == self.head:  # 원형 리스트의 끝을 만남
                    break
            print(" <-> ".join(map(str, values)))
