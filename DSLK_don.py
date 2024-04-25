from DSSV import read_student_data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class dslk_don:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def search_students(self, criteria, keyword):
        search_results = []
        current_node = self.head
        while current_node:
            student = current_node.data
            if getattr(student, criteria.lower(), None) and keyword.lower() in getattr(student, criteria.lower()).lower():
                search_results.append(student)
            current_node = current_node.next
        return search_results

