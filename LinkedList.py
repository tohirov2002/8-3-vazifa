
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def counts(self):
        count = 0
        current = self.head
        while current:
            if isinstance(current.data, int) and current.data % 2 == 0:
                count += 1
            current = current.next
        return count

    def string_sanash(self, target_string):
        occurrences = []
        index = 0
        current = self.head
        while current:
            if isinstance(current.data, str) and target_string == current.data:
                occurrences.append(index)
            current = current.next
            index += 1
        return occurrences

    def append_list(self, data_list):
        for item in data_list:
            self.append(item)

    def remove(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()




