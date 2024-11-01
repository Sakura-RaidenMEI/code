class BPlusTreeNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.children = []
        self.is_leaf = True

# Define a class for the BPlusTree
class BPlusTree:
    # Initialize the BPlusTree with a given order
    def __init__(self, order):
        self.root = None  # Root of the tree
        self.order = order  # Order of the B+ tree

    # Function to insert a key into the BPlusTree
    def insert(self, key):
        # Logic to insert the key while maintaining B+ tree properties
        pass  # Placeholder for insertion logic

    # Function to print the BPlusTree
    def print_tree(self):
        # Call the recursive function to print the tree
        self._print_tree(self.root)

    # Recursive function to print the tree nodes
    def _print_tree(self, node):
        if node is not None:
            # Print the keys in the current node
            print(node.keys)  # Print the keys of the current node
            # Recursively print the children nodes
            for child in node.children:
                self._print_tree(child)

# Example usage of the BPlusTree class
bpt = BPlusTree(order=3)  # Create a BPlusTree with order 3
bpt.insert(10)  # Insert key 10
bpt.insert(20)  # Insert key 20
bpt.print_tree()  # Print the BPlusTree

# Main function that tests the BPlusTree class
def main_BPlusTree():
    # Create a BPlusTree instance
    bpt = BPlusTree(order=3)
    # Use case 1: Insert keys and print the tree
    bpt.insert(10)
    bpt.insert(20)
    bpt.print_tree()  # Expected to print the structure of the tree
    # Use case 2: Insert more keys and print the tree
    bpt.insert(30)
    bpt.insert(40)
    bpt.print_tree()  # Expected to show updated structure of the tree

# Call the main function to execute the test cases
main_BPlusTree()