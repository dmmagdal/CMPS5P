class LinkedList:
    class Node:
        
        def Node(num):
            val = int(num)
            next = null

    def LinkedList():
        head = null
        numItems = 0

    def insert(num):
        N = Node(num)
        N.next = head
        head = N
        numItems += 1

    def delete(num):
        N = head
        Prev = head
        while N.next != null:
            if N.val == num:
                while Prev != N:
                    Prev = Prev.next
                Prev.next = N.next
                numItems -=1
                break
            N = N.next

    def size():
        return numItems

    def printList():
        N = head
        while N.next != null:
            print(N.val+" ", End="")
            N = N.next


if __name__ == "__main__":
    L = LinkedList()
    L.insert(1)
    L.insert(5)
    L.insert(9)

    L.printList()

    L.delete(1)

    L.printList()

    L.insert(4)
    L.insert(2)
    L.insert(7)

    L.printList()

    L.delete(4)
    L.delete(7)

    L.printList()
    print(L.size())
