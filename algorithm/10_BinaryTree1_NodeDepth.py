class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1
# size와 다른 점은 depth는 가장 깊은 노드를 말하는 것이고 size는 전체 노드 개수를 말하는 것임
# 특정 노드가 루트노드인 서브트리의 깊이를 구하는 함수


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        return self.root.depth() if self.root else 0
# 트리의 깊이를 구하는 함수

def solution(x):
    return 0