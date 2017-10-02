# trie
An example implementation of Trie data structure for implementing fast searches of a given string.
Value of a node is ignored as the sole purpose is to search for strings prefixing given terms.

To run use the below command:
```bash
python auto_complete.py --file test --key p
```

Note that space usage is rather huge as every node has a 256 length list each corresponding to a character's ASCII code.
For reducing space cost, ternary tree implementation could have used.

If it was required to make a substring search, different algorithms would have been used, such as `Boyer-Moore` or
`Rabin-Karp Fingerprint` or `Knuth-Morris-Pratt`.