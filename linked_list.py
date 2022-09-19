class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_at_end(self, data):
        if self.head is None:
            print(data)
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
            print("ittt herer ",itr.data)

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    # ll.insert_at(1,"blueberry")
    # ll.remove_at(2)
    ll.print()

    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()