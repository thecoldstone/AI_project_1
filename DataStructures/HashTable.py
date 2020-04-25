INITIAL_CAPACITY = 303

""" 'X Y' : (1,2,3) 
    'X1 Y2: (1, 2)'"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)

class HashTable:

    def __init__(self, hashTableSize = INITIAL_CAPACITY):
        self.capacity = hashTableSize
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):

        hashSum = 0

        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashSum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashSum = hashSum % self.capacity

        return hashSum

    def insert(self, key, value):

        #1. Increment size
        self.size += 1
        #2. Compute index of key
        index = self.hash(key)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        #3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            return

        #4. Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next

        # Add a new node at the end of the list with provided key/value
        prev.next = Node(key, value)

    def find(self, key):

        #1. Compute index of key
        index = self.hash(key)
        #2. Go to the first node in list at bucke
        node = self.buckets[index]
        #3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next

        #4. Now, node is the requested key/value pair or None
        if node is None:
            return None
        else:
            return node

    def getValuesOfKey(self, key):

        # 1. Compute index of key
        index = self.hash(key)
        # 2. Go to the first node in list at bucke
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next

        # 4. Now, node is the requested key/value pair or None
        if node is None:
            return None
        else:
            list = []
            while node is not None:
                list.append(node.value)
                node = node.next
            return list

    def remove(self, key):
        # 1. Compute index of key
        index = self.hash(key)
        # 2. Go to the first node in list at bucke
        node = self.buckets[index]
        prev = None
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            prev = node
            node = node.next

        # Now, node is either the requested node or None
        if node is None:
            #4. Key not found
            return None
        else:
            #5. The key was found
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next # May be None, or the next match
            else:
                prev.next = prev.next.next

            return result

    #TODO

    # def removeAll(self):
    #     for i in range(0, INITIAL_CAPACITY):
    #
    #         node = self.buckets[i]
    #         prev = node
    #
    #         if node is None:
    #             continue
    #
    #         while node is not None:
    #             node = node.next


    def printHashTable(self):

        print("HashTable looks like:\n=====================")

        for i in range(0, INITIAL_CAPACITY):

            node = self.buckets[i]

            if node is None:
                continue

            print(str(node.key) + ": ", end="")
            while node is not None:
                print(node.value, end="")
                if node.next is not None:
                    print(",", end="")
                node = node.next

            print()
