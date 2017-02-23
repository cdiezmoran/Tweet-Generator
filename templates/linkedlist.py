#!python

#from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)

        if self.tail == None and self.head == None:
            self.tail = new_node
            self.head = new_node
        elif self.tail == self.head:
            self.tail = new_node
            self.head.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)

        if self.head == None and self.tail == None:
            self.tail = new_node
            self.head = new_node
        elif self.head == self.tail:
            self.head = new_node
            self.head.next = self.tail
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        current = self.head
        last_node = None

        while  (current is not None) and (current.data is not item):
            last_node = current
            current = current.next

        print "Current after while: %s\n" % (current)

        if current is None:
            raise ValueError("Could not find %s in List." % (item))

        if current == self.head and current == self.tail:
            self.head = None
            self.tail = None
        elif current == self.head:
            self.head = current.next
            current.next = None
        elif current == self.tail:
            self.tail = last_node
            last_node.next = None
        else:
            last_node.next = current.next
            current.next = None


        return 'Deleted item'

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        current = self.head

        while current is not None:
            if quality(current.data):
                return current.data
            current = current.next

        return None


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    # Enable this after implementing delete:
    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
