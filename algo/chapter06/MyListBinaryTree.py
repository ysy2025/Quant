class MyListBinaryTree:  # 通过list实现的tree结构
    # 初始化一个二叉树
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

        self.binary_tree = [self.root, self.left, self.right]

    # 判断二叉树是否为空树
    def is_empty(self):
        return len(self.binary_tree) == 0

    # 判断是不是叶子结点(是否嵌套了子list);节点中有list类型,就说明有子树,返回True;反之返回false,没有嵌套子list
    def is_nested(self):
        content_sum = 0
        for each in self.binary_tree:
            if isinstance(each, MyListBinaryTree):
                content_sum += 1
        return True if content_sum else False

    # 输出二叉树
    def print_all(self):
        # 初始化输出list
        res = []

        # 递归输出;结束递归的条件
        # 叶子节点,直接输出btree
        if not self.is_nested(): # 没有嵌套
            res += self.binary_tree
        else: # 嵌套了
            # 首先获得root,left,right
            root = self.get_root()
            left = self.get_left()
            right = self.get_right()

            print("root is {0}, type is {1}".format(root, type(root)))
            print("left is {0}, type is {1}".format(left, type(left)))
            print("right is {0}, type is {1}".format(right, type(right)))

            res.append(root)
            if left is None:
                res.append(left)
                pass
            else:
                res_left = left.print_all()
                res .append(res_left)
            if right is None:
                res.append(right)
                pass
            else:
                res_right = right.print_all()
                res.append(res_right)

        #     res += [root]
        #     res.append(left)
        #     res.append(right)
        #
        print("res is {0}".format(res))
        return res

    # 求二叉树的节点个数
    def num_nodes(self):
        pass

    # 获取根节点数据
    def get_root(self):
        return None if self.is_empty() else self.binary_tree[0]

    # 获取左子树数据
    def get_left(self):
        return self.binary_tree[1]

    # 获取右子树数据
    def get_right(self):
        return self.binary_tree[2]

    # 设置root节点
    def set_root(self, new_root):
        self.root = new_root
        self.binary_tree[0] = new_root
        return self.binary_tree

    # 用btree取代左子树
    def set_left(self, btree):
        self.left = btree
        self.binary_tree[1] = btree
        return self.binary_tree

    # 用btree取代右子树
    def set_right(self, btree):
        self.right = btree
        self.binary_tree[2] = btree
        return self.binary_tree

    # 遍历二叉树各个节点数据的迭代器
    def traversal(self):
        pass

    # 对二叉树中每个节点的数据执行操作 operation
    def forall(self, operation):
        pass


if __name__ == '__main__':
    myTree = MyListBinaryTree(10, MyListBinaryTree(20, MyListBinaryTree(20, 30, 30)), MyListBinaryTree(20, 20, 320))
    print(myTree.is_nested())
    print(myTree.get_left().is_nested())
    print(myTree.get_right().is_nested())
    myTree.print_all()
    # print(myTreeList)

    myTree2 = MyListBinaryTree(10,  300, 320)
    myTree2.print_all()