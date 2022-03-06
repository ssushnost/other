class TreeNode:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


class SplayTree:
    def __init__(self):
        self.root = None
        self.search_bool = False

    def put(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = TreeNode(key)

    def _put(self, key, cur_node):
        if key < cur_node.key:
            if cur_node.hasLeftChild():
                self._put(key, cur_node.leftChild)
            else:
                cur_node.leftChild = TreeNode(key, parent=cur_node)
                self.splay(cur_node.leftChild)
        elif key > cur_node.key:
            if cur_node.hasRightChild():
                self._put(key, cur_node.rightChild)
            else:
                cur_node.rightChild = TreeNode(key, parent=cur_node)
                self.splay(cur_node.rightChild)
        else:
            print('Node exist')

    def splay(self, cur_node):
        while not cur_node.isRoot():
            if cur_node.parent.isRoot():
                if cur_node.isLeftChild():
                    '''zig'''
                    self.rotateRight(cur_node.parent)
                else:
                    '''zag'''
                    self.rotateLeft(cur_node.parent)
            else:
                par = cur_node.parent
                grand_par = par.parent
                if cur_node.isLeftChild() and par.isLeftChild():
                    '''zig-zig'''
                    self.rotateRight(grand_par)
                    self.rotateRight(par)
                elif cur_node.isRightChild() and par.isRightChild():
                    '''zag-zag'''
                    self.rotateLeft(grand_par)
                    self.rotateLeft(par)
                elif cur_node.isLeftChild() and par.isRightChild():
                    '''zig-zag'''
                    self.rotateRight(par)
                    self.rotateLeft(grand_par)
                else:
                    '''zag-zig'''
                    self.rotateLeft(par)
                    self.rotateRight(grand_par)

    def rotateRight(self, cur_node):
        temp = cur_node.leftChild
        cur_node.leftChild = temp.rightChild
        if temp.rightChild is not None:
            temp.rightChild.parent = cur_node
        temp.parent = cur_node.parent
        if cur_node.isRoot():
            self.root = temp
        else:
            if cur_node.isRightChild():
                cur_node.parent.rightChild = temp
            else:
                cur_node.parent.leftChild = temp
        temp.rightChild = cur_node
        cur_node.parent = temp

    def rotateLeft(self, cur_node):
        temp = cur_node.rightChild
        cur_node.rightChild = temp.leftChild
        if temp.leftChild is not None:
            temp.leftChild.parent = cur_node
        temp.parent = cur_node.parent
        if cur_node.isRoot():
            self.root = temp
        else:
            if cur_node.isLeftChild():
                cur_node.parent.leftChild = temp
            else:
                cur_node.parent.rightChild = temp
        temp.leftChild = cur_node
        cur_node.parent = temp

    def print_tree_inOrder(self):
        if self.root is not None:
            self._print_tree_inOrder(self.root)
        else:
            print('Tree Is Empty')

    def _print_tree_inOrder(self, cur_node):
        if cur_node is not None:
            self._print_tree_inOrder(cur_node.leftChild)
            print(cur_node.key)
            self._print_tree_inOrder(cur_node.rightChild)

    def print_tree_postOrder(self):
        if self.root is not None:
            self._print_tree_postOrder(self.root)
        else:
            print('Tree Is Empty')

    def _print_tree_postOrder(self, cur_node):
        if cur_node is not None:
            self._print_tree_postOrder(cur_node.leftChild)
            self._print_tree_postOrder(cur_node.rightChild)
            print(cur_node.key)

    def maxim(self):
        if not self.root:
            print('Tree Is Empty')
        else:
            self._maxim(self.root)

    def _maxim(self, cur_node):
        if cur_node.hasRightChild():
            self._maxim(cur_node.rightChild)
        else:
            print(cur_node.key)

    def minim(self):
        if not self.root:
            print('Tree Is Empty')
        else:
            self._minim(self.root)

    def _minim(self, cur_node):
        if cur_node.hasLeftChild():
            self._minim(cur_node.leftChild)
        else:
            print(cur_node.key)

    def search(self, key, cur_node):
        if cur_node:
            if cur_node.key == int(key):
                self.search_bool = True
                self.splay(cur_node)
            elif cur_node.key > int(key):
                self.search(key, cur_node.leftChild)
            elif cur_node.key < int(key):
                self.search(key, cur_node.rightChild)


    def print_tree_preOrder(self):
        if self.root is not None:
            self._print_tree_preOrder(self.root)
        else:
            print('Tree Is Empty')

    def _print_tree_preOrder(self, cur_node):
        if cur_node:
            print(cur_node.key)
            self._print_tree_preOrder(cur_node.leftChild)
            self._print_tree_preOrder(cur_node.rightChild)

    def height(self, cur_node):
        if not cur_node:
            return 0
        else:
            return max(self.height(cur_node.leftChild), self.height(cur_node.rightChild)) + 1

    def get_size(self):
        if self.root:
            self.size = self._get_size(self.root)
            print(self.size)
        else:
            print('Tree Is Empty')

    def _get_size(self, cur_node):
        if not cur_node:
            return 0
        else:
            return self._get_size(cur_node.leftChild) + self._get_size(cur_node.rightChild) + 1

    def get_root(self):
        if not self.root:
            print('Tree Is Empty')
        else:
            print(self.root.key)


bst = SplayTree()
while True:
    inp = input().split()
    if inp[0] == 'insert':
        bst.put(int(inp[1]))
    elif inp[0] == 'find':
        bst.search_bool = False
        bst.search(inp[1], bst.root)
        print(bst.search_bool)
    elif inp[0] == 'height':
        print(bst.height(bst.root))
    elif inp[0] == 'size':
        bst.get_size()
    elif inp[0] == 'min':
        bst.minim()
    elif inp[0] == 'root':
        bst.get_root()
    elif inp[0] == 'max':
        bst.maxim()
    elif inp[0] == 'print' and inp[1] == 'inOrder':
        bst.print_tree_inOrder()
    elif inp[0] == 'print' and inp[1] == 'preOrder':
        bst.print_tree_preOrder()
    elif inp[0] == 'print' and inp[1] == 'postOrder':
        bst.print_tree_postOrder()
    elif inp[0] == 'stop':
        break
    else:
        print('wrong command')
