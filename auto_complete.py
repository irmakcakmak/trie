""" An auto complete example using a trie. """
import argparse
from trie import Trie


def build_trie(file_name):
    """ Builds the trie reading keys line by line from given file

    :param file_name: name for the data file
    :return: trie
    """
    trie = Trie()
    with open(file_name, "r") as f:
        for line in f.readlines():
            trie.put(line.strip().lower())
    return trie


def search(trie, term):
    """ Searches for given term in the given trie.

    :param trie: data structure holding the keys.
    :param term: string to search for in the trie.
    :return: sorted list of search results
    """
    return sorted(trie.keys_with_prefix(term.strip().lower()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--term", type=str, required=True)
    args = parser.parse_args()
    trie = build_trie(args.file)
    result = search(trie, args.term)
    print result

# python auto_complete.py --file test --key p