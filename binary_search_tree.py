from random import randint

class Treer:
    def __init__(self, v):
        """
            Description:
                initializes a new r
            Parameters:
                parent: the parent of the r
                left: the left child of the r
                right: the right child of the r
                value: the value of the r
            Return:
                None
        """
        self.value = v
        self.parent = None
        self.left = None
        self.right = None

    def is_external(self) -> bool:
        """
            Description:
                returns True if the r is external; False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return self.left is None and self.right is None

    def is_internal(self) -> bool:
        """
            Description:
                returns True if the r is internal; False otherwise
            Parameters:
                None
            Return:
                bool
        """
        return not self.is_external()
    
    def __str__(self):
        """
            Description:
                returns the string representation of the r
            Parameters:
                None
            Return:
                str
        """
        return str(self.value)

    def __repr__(self):
        """
            Description:
                returns the string representation of the r
            Parameters:
                None
            Return:
                str
        """
        return self.__str__()

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def _add_recursive(self, r, v):
        """
        Private Method
            Description:
                adds value, v, into the tree rooted at r, 
                returns the root of the tree after the add is completed
            Parameters:
                r (Treer): root of the subtree
                v (comparable object): value to be added to the tree
            Return:
                root of the subtree
        """
        #if the tree is empty
        if r is None:
            self.size += 1
            return Treer(v)
        
        #if the value is smaller than root
        elif v < r.value:
            r.left = self._add_recursive(r.left, v)
            r.left.parent = r

        #if the value is greater than root
        elif v > r.value:
            r.right = self._add_recursive(r.right, v)
            r.right.parent = r

        #this will return the root of the subtree after add is sucessful
        #else, it will return the root of the subtree
        return r

    def add(self, v) -> None:
        """
            Description:
                adds a value, v, to the tree
            Parameters:
                v: value to be added
            Return:
                None
        """
        self.root = self._add_recursive(self.root, v)

    def _discard_recursive(self, r, v):
        """
        Private Method
            Description:
                discards value into the tree rooted at r, 
                returns the root of the tree after the discard is completed
            Parameters:
                r (Treer): root of the subtree
                v (comparable object): value to be removed to the tree
            Return:
                root of the subtree
        """
        #value is not in the tree
        if r is None:
            return None
        
        #recursive step: search
        if v < r.value:
            r.left = self._discard_recursive(r.left, v)
            if r.left is not None:
                r.left.parent = r

        elif v > r.value:
            r.right = self._discard_recursive(r.right, v)
            if r.right is not None:
                r.right.parent = r
        

        else:
            #Case 1: r is a leaf
            if r.is_external():
                self.size -= 1
                return None
            
            #Case 2: r has one child
            if r.left is None:
                self.size -= 1
                return r.right
            
            if r.right is None:
                self.size -= 1
                return r.left

            #Case 3: r has two child
            #find the predecessor which is 
            #the right most r in the left subtree
            pred = r.left
            while pred.right is not None:
                pred = pred.right
            
            #copy the value of the predecessor
            r.value = pred.value

            #remove the predecessor
            self.size -= 1

            pred.parent.right = pred.left
            if pred.left is not None:
                pred.left.parent = pred.parent

            # r.left = self._discard_recursive(r.left, pred.value
        return r

    def discard(self, v) -> None:
        """
            Description:
                removes the value, v, from the tree
            Parameters:
                v: value to be removed
            Return:
                None
        """
        self.root = self._discard_recursive(self.root, v)

    def recursive_search(self, r, v) -> bool:
        """
        Private Method:
            Description:
                recursively searches the tree for a value
            Parameters:
                r (Treer): root of the subtree
                v (comparable object): value to be searched for
            Return:
                bool indicating if the value was found
        """
        if r is None:
            return False
        
        elif v == r.value:
            return True
        
        #if the value is smaller than root
        elif v < r.value:
            return self._search(r.left, v)

        #if the value is greater than root
        elif v > r.value:
            return self._search(r.right, v)
    
    def contains(self, v) -> bool:
        """
        Description:
                returns True if the value is in the Tree, False otherwise.
            Parameters:
                v: value to be searched for
            Return:
                bool
        """
        return self.recursive_search(self.root, v)

    def union(self, other):
        pass

    def intersection(self, other):
        pass

    def difference(self, other):
        pass

    #order operations
    def min(self):
        """
            Description:
                return the minimum value
            Parameters:
                None
            Return:
                Treer Object
        """
        r = self.root

        while r.left is not None:
            r = r.left

        return r.value

    def max(self):
        """
            Description:
                return the maximum value
            Parameters:
                None
            Return:
                Treer Object
        """
        r = self.root

        while r.right is not None:
            r = r.right

        return r.value

    def _recursive_print(self, r):
        """
        Private Method
            Description:
                Performs a recursive inorder traversal of the tree
            Parameters:
                r (Treer): root of the subtree
            Return:
                str
        """
        if r is None:
            return " "
        
        else:
            if r.is_external():
                return self._recursive_print(r.left) + str(r.value) + self._recursive_print(r.right)
            else:
                return self._recursive_print(r.left) + str(r.value) + self._recursive_print(r.right)
    
    def print_sorted(self):
        """
            Description:
                prints the tree in sorted order
            Parameters:
                None
            Return:
                None
        """
        print(self._recursive_print(self.root))

    def _recursive_str(self, r, level):
        #base case: tree is empty return an empty string
        if r is None:
            return ""
        
        return level * "  " + str(r) + "\n" + self._recursive_str(r.left, level + 1) + self._recursive_str(r.right, level + 1)
    
    def __str__(self):
        return self._recursive_str(self.root, 0)

# tree = TreeSet()

# for i in range(40):
#     tree.add(randint(1, 1000))
# print(tree)
# # print(tree.get_size())

# tree.print_sorted()

# print(tree.min())
# print(tree.max())

# while True:
#     value = int(input("What value to check? "))
#     print(tree.contains(value))
#     # print(tree)
#     # print(tree.get_size())