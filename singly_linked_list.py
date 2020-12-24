class Node:
    '''
    Used for creating the nodes used in a singly linked list.
    '''

    def __init__(self, val, next=None):
        '''
        Initialize attributes to describe a singly linked node.
        '''
        self.val = val
        self.next = next


class SLL:
    '''
    Data structure where each node has a reference to it's next node.
    '''

    def __init__(self):
        '''
        Initialize attributes to describe a singly linked list.
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, val):
        """
        Adds a value to the end of the linked list.
        """
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return self.length

    def add_multiple(self, *values):
        """
        Adds multiple values by calling add method.
        """
        for val in values:
            self.add(val)
        return self

    def to_list(self):
        """
        Returns a simple list/array of values in the linked list.
        """
        # Rename unlink?
        values = []
        node = self.head

        while node:
            values.append(node.val)
            node = node.next

        return values

    def pop(self, index):
        """
        Removes and returns an element of the list, zero indexed.
        """
        current = self.head
        holder = self.head

        if self.length <= 0 or self.length <= index:
            return None

        elif index == 0:
            self.head = current.next

        else:
            for num in range(0, index):
                holder = current
                current = current.next

        holder.next = current.next
        self.length -= 1
        return current

    def insert(self, val, index):
        """
        Inserts a value anywhere within the list, zero indexed.
        """
        if index >= self.length - 1 or index < 0:
            return False
        elif self.length == 0:
            self.add(val)

        current = self.head
        prev = None

        for num in range(0, index):
            prev = current
            current = current.next

        prev.next = Node(val, current)
        self.length += 1
        return self.length

    def index_of(self, val):
        """
          Returns the index of the first occurrence of a value in the list or false if value is not in list. 
        """
        current = self.head
        count = 0

        while current:
            if current.val == val:
                return count
            else:
                count += 1
                current = current.next

        return False

    def reverse(self):
        '''
        Reverses and returns list.
        '''

        node = self.head
        prev = None
        temp = None
        [self.head, self.tail] = [self.tail, self.head]

        for num in range(0, self.length):
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return self

    def sort(self):
      """
      Sort takes the values of the linked list and returns
      a sorted new linked list, doesn't mutate original list.
      """
      
      arg_list = self.to_list()
      arg_list.sort()
      new_list = SLL().add_multiple(*arg_list)
      return new_list

my_list = SLL()

my_list.add_multiple(34,46,58,19,5,29,35)
my_list = my_list.sort()
print(my_list.to_list())
# print(my_list.length)
