from LinkedList import LinkedList


class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):
        array = [None] * size
        for i in range(len(array)):
            array[i] = LinkedList()
        return array

        # 2️⃣ TODO: Create your own hash function.

        # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored.

    def hash_func(self, key):

        return hash(key) % len(self.arr)

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        index = self.hash_func(key)
        print(self.arr[index], index)
        found_item = self.arr[index].find(lambda item: item[0] == key)
        new_item = (key, value)
        if found_item == True:
            self.arr[index].replace(found_item, new_item)
        else:
            self.arr[index].append(new_item)

    # 4️⃣ TODO: Complete the print_key_values method.

    # Traverse through the every Linked List in the table and print the key value pairs.

    # For example:
    # a: 1
    # again: 1
    # and: 1
    # blooms: 1
    # erase: 2

    def print_key_values(self):
        for linked_list in self.arr:
            print(linked_list.print_nodes())
