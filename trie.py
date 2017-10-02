""" Simple Trie implementation for string search. """
RADIX = 256


class Node(object):
    """
        Class representing a node in the trie.
    """

    def __init__(self):
        self.next = [None] * RADIX
        self.size = 0


class Trie(object):
    """
        A symbol table implementation for string search.
    """

    def __init__(self):
        self._root = Node()

    def _get(self, node, key, index):
        """ Recursively finds the node with the given key

        :param node: current node
        :param key: search key
        :param index: key's correlating character's index with the current node
        :return:
        """
        if node is None:
            return None
        if index == len(key):
            return node
        order = ord(key[index])
        return self._get(node.next[order], key, index+1)

    def get(self, key):
        """ Returns the node matching with the key.

        :param key: Search key.
        :return:
        """
        result = self._get(self._root, key, 0)
        return result

    def _put(self, node, key, index):
        """ Recursively inserts the given key to trie.

        :param node: Current node
        :param key: Whole key to be inserted
        :param index: Index of the char of key corresponding the the current node
        :return: current node
        """
        if node is None:
            node = Node()
        if index == len(key):
            return node
        order = ord(key[index])
        node.next[order] = self._put(node.next[order], key, index+1)
        node.size += 1
        return node

    def put(self, key):
        """ Inserts given key.

        :param key: Key to be inserted.
        """
        self._root = self._put(self._root, key, 0)

    def _collect(self, node, pre, queue):
        """ Recursively build representation of the string from root to end node.

        :param node: current node
        :param pre: prefix to search for
        :param queue: queue keeping the matching keys
        :return:
        """
        if node is None:
            return
        if node.size == 0:
            queue.insert(0, pre)
        for i in range(0, RADIX):
            self._collect(node.next[i], pre + chr(i), queue)

    def keys_with_prefix(self, prefix):
        """ Finds keys matching with the given prefix.

        :param prefix: prefix to keys.
        :return: queue of matching keys
        """
        queue = []
        self._collect(self._get(self._root, prefix, 0), prefix, queue)
        return queue
