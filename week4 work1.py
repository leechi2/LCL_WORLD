# Min Heap 자료구조를 이용하면 최대값을 O(logN)의 시간복잡도로 찾을 수 있다.
# Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는
# Priority Queue를 구현할 수 있다. Min Heap을 이용한 Priority Queue는 아래와 같은 특징을 가진다.
#
# Min Heap을 이용한 Priority Queue의 특징
# 자료를 입력하는 동작과 출력하는 동작 모두 O(logN)으로 이루어진다.
# 우선순위 값이 낮은 자료를 먼저 반환하되, 우선순위 값이 같은 자료끼리는 순서를 고려하지 않는다.
# 다음과 같은 Method들을 구현한다.
# is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 반환한다.
# put(): Priority Queue에 우선순위와 자료를 (우선순위, 자료) 형태의 Tuple로 입력받는다.
# get(): Priority Queue에서 자료를 반환한다. 출력한 데이터는 Priority Queue에서 삭제한다. 더이상 반환할 데이터가 없는 경우 None을 반환한다.
# peek(): Priority Queue에서 자료를 반환한다. 반환한 데이터는 Priority Queue에 그대로 유지한다. 더이상 반환할 데이터가 없는 경우 None을 반환한다.

class PriorityQueue:
    def __init__(self):
        self.heap_array = list()
        self.heap_array.append(None)


    def is_empty(self):
        if len(self.heap_array) <= 1:
            return print(False)
        else:
            return print(True)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx][0] < self.heap_array[parent_idx][0]:
            return True
        else:
            return False

    def put(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                return True
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx][0] < self.heap_array[right_child_popped_idx][0]:
                if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx][0] > self.heap_array[right_child_popped_idx][0]:
                    return True
                else:
                    return False

    def get(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx][0] < self.heap_array[right_child_popped_idx][0]:
                    if self.heap_array[popped_idx][0] > self.heap_array[left_child_popped_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx][0] > self.heap_array[right_child_popped_idx][0]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx],self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx

        return returned_data



    def peek(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        return returned_data


# Test code

pq = PriorityQueue()
pq.is_empty()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
pq.is_empty()

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
