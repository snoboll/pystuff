coins = [1,2,5,10,20,50]

class TreeNode():

    def __init__(self, val):
        self.val = val
        self.one = TreeNode(val)