# pramp question

# Time Complexity: O(n)
# Space Complexity: O(n)
def inorder_traverse(root):
    nodes_list = []

    def traverse(root):
        if not root:
            return

        traverse(root.left)
        nodes_list.append(root)
        traverse(root.right)

    traverse(root)

    return nodes_list


# A node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    # Time complexity: O(n)
    # Space Complexity: O(n)
    def find_largest_smaller_key(self, num):
        result = -1
        nodes_list = inorder_traverse(self.root)
        nodes_values = []

        for node in nodes_list:
            nodes_values.append(node.key)

        for i, value in enumerate(nodes_values):
            if num == nodes_values[i] and i >= 1:
                result = nodes_values[i - 1]
                break

        return result

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while currentNode is not None:
            if key < currentNode.key:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################
if __name__ == '__main__':
    bst = BinarySearchTree()

    # Create the tree given in the above diagram
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    result = bst.find_largest_smaller_key(25)

    print(result)
