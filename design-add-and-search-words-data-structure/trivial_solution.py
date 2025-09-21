from utils.trie_utils import TrieNode


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # Time complexity: O(m), where m is the length of the word.
    # Space complexity: O(m)
    def addWord(self, word: str) -> None:
        node = self.root
        # Traverse the trie, creating nodes for each character in the word
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node corresponding to the character
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:

        # Helper function to search in the trie recursively
        # Time complexity: O(m) - when the word does not contain any dots
        # Space complexity: O(1) - no additional space used for the search

        # if the word contains dots, we will explore all possible paths
        # Time complexity: O(26^m) where d is the number of dots in the word
        # Space complexity: O(m) for the recursion stack

        def search_in_node(node: TrieNode, word_index: int) -> bool:
            # If we have reached the end of the word, check if we are at the end of a valid word
            for index in range(word_index, len(word)):
                char = word[index]

                # If the current character is a wildcard (dot), we need to validate the rest of the word
                if char == '.':
                    for child in node.children.values():  # iterate through all children in the children dictionary
                        if search_in_node(child, index + 1):
                            return True
                    return False

                # If the character is not a wildcard, we check if it exists in the current node's children
                elif char in node.children:
                    # move to the child node
                    node = node.children[char]
                else:
                    return False
            # If we reach here, it means we have matched all characters in the word,
            # so we need to check if we are at the end of a word
            return node.is_end_of_word

        # Start the search from the root node, and from the first character of the word
        return search_in_node(self.root, 0)


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))
    print(wordDictionary.search("bad"))
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("b.."))
