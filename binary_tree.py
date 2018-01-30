class VALUE(object):
    def __init__(self,number=0,string='',dictionary={},list=[]):
        self.number = number
        self.string = string
        self.dictionary = dictionary
        self.list = list
class NODE(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def Get_value():
    inputlist = input('''Please enter the value of node.
    (Format:number-string-the key of dictionary-the value of dictionary-the list)\n''').split('-')
    return (eval(inputlist[0]),inputlist[1],dict(zip(eval(inputlist[2]),eval(inputlist[3]))),eval(inputlist[4]))
def Create_binary_tree(root):
    try:
        root = NODE(VALUE(*(Get_value())))
    except:
        print("OVERFLOW: No room availible!\n")
        exit(0)
    if int(input("Is there a left leave of the node? (1 for Y,0 for N).\n")):
        Create_binary_tree(root.left)
    if int(input("Is there a right leave of the node? (1 for Y,0 for N).\n")):
        Create_binary_tree(root.right)
    return root
def Preorder_traversal(root):
    if not root:
        return None
    '''operate root  here'''
    Preorder_traversal(root.left)
    Preorder_traversal(root.right)
    print("Preorder traversal finished.\n")
    return None
def Postorder_travelsal(root):
    if not root:
        return None
    Postorder_travelsal(root.left)
    Postorder_travelsal(root.right)
    '''operate root  here'''
    print("Postorder traversal finished.\n")
    return None
def Inorder_travelsal(root):
    if not root:
        return None
    Inorder_travelsal(root.left)
    '''operate root  here'''
    Inorder_travelsal(root.right)
    print("Inorder traversal finished.\n")
    return None
