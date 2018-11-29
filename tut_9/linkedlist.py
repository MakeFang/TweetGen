#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.iter = self.head
        self.lengths = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # node = self.head
        # count = 0
        # while node is not None:
        #     count += 1
        #     node = node.next
        # return count
        return self.lengths

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        end_node = Node(item)
        if self.tail is not None:
            self.tail.next = end_node
            self.tail = end_node
        # if self.head is None and self.tail is None:
        elif self.head is None:
            self.head = end_node
            self.tail = end_node
            self.iter = self.head
        self.lengths += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        start_node = Node(item)
        if self.head is None:
            self.head = start_node
            self.tail = start_node
        else:
            start_node.next = self.head
            self.head = start_node
        self.iter = self.head
        self.lengths += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            if cur_node.data == item:
                self.lengths -= 1
                if cur_node.next is None:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next = cur_node.next
                    return self.head
                else:
                    self.head = cur_node.next
                    return self.head
            prev_node = cur_node
            cur_node = cur_node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return node.data
            node = node.next
        # self.append(new_item)
        # return self.head
        raise ValueError('Item not found: {}'.format(item))

    def update_append(self, quality, item):
        """Running time is O(n) where n is the length of the linked list.
        However, if quality has some time complexity O(g(x)), then the runtime
        would be O(n*g(x))."""
        node = self.head
        while node is not None:
            if quality(node.data):
                node.data = item
                return node.data
            node = node.next
        self.append(item)
        return self.head

    def delete_q(self, quality):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        Worst case and average running time O(n) since the method
        loops through the linked list once to do the search and delete. Here
        n is the length of the linked list.
        However, if quality has some time complexity O(g(x)), then the runtime
        would be O(n*g(x))."""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            if quality(cur_node.data):
                self.lengths -= 1
                if cur_node.next is None:
                    self.tail = prev_node
                if prev_node is not None:
                    prev_node.next = cur_node.next
                    return True
                else:
                    self.head = cur_node.next
                    return True
            prev_node = cur_node
            cur_node = cur_node.next
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter is not None:
            result = self.iter
            self.iter = self.iter.next
            return result
        else:
            self.iter = self.head
            raise StopIteration


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    for item in ll:
        print(item)

    # ll.replace('A', 'X')
    # print('list: {}'.format(ll))
    # ll.replace('X', 'C')
    # print('list: {}'.format(ll))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
