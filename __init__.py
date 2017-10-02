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

    def _collect(self, node, pre, queue):
        if node is None:
            return
        queue.insert(0, pre)
        for i in range(0, RADIX):
            self._collect(node.next[i], pre + chr(i), queue)

    def keys_with_prefix(self, prefix):
        queue = []
        self._collect(self._get(self._root, prefix, 0), prefix, queue)
        return queue

if __name__ == '__main__':
    trie = Trie()
    trie.put("hede")
    trie.put("hebelek")
    trie.put("foo")
    trie.put("bar")
    result = trie.keys_with_prefix("he")
    print result