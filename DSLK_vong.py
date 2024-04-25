from DSSV import read_student_data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class dslk_vong:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head
        
    def search_students(self, criteria, keyword):
        search_results = []
        current_node = self.head
        while current_node:
            student = current_node.data
            if criteria == 'Mã sinh viên' and keyword.lower() in student.Mã_SV.lower():
                search_results.append(student)
            elif criteria == 'Họ' and keyword.lower() in student.Họ_lót.lower():
                search_results.append(student)
            elif criteria == 'Tên' and keyword.lower() in student.Tên.lower():
                search_results.append(student)
            elif criteria == 'Lớp' and keyword.lower() in student.Mã_lớp.lower():
                search_results.append(student)
            elif criteria == 'Điểm' and keyword.lower() in str(student.Điểm).lower():
                search_results.append(student)
            current_node = current_node.next
        return search_results
