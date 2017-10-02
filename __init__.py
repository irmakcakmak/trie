RADIX = 256


class Node(object):
    def __init__(self):
        self.next = [None] * RADIX


class Trie(object):
    def __init__(self):
        self._root = Node()

    def _get(self, node, key, index):
        if node is None:
            return None
        if index == len(key):
            return node
        order = ord(key[index])
        return self._get(node.next[order], key, index+1)

    def get(self, key):
        result = self._get(self._root, key, 0)
        return result

    def _put(self, node, key, index):
        if node is None:
            node = Node()
        if index == len(key):
            return node
        order = ord(key[index])
        node.next[order] = self._put(node.next[order], key, index+1)
        return node

    def put(self, key):
        self._root = self._put(self._root, key, 0)

if __name__ == '__main__':
    trie = Trie()
    trie.put("hede")
    result = trie.get("hede")
    result = trie.get("he")
    result = trie.get("bar")
    print result