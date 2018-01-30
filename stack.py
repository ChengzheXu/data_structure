class VALUE(object):
    def __init__(self,number=0,string='',dictionary={},list=[]):
        self.number = number
        self.string = string
        self.dictionary = dictionary
        self.list = list
class NODE(object):
    def __init__(self,value,nextprt=None):
        self.value = value
        self.nextprt = nextprt
def Get_value():
    inputlist = input('''Please enter the value of node.
    (Format:number-string-the key of dictionary-the value of dictionary-the list)\n''').split('-')
    return (eval(inputlist[0]),inputlist[1],dict(zip(eval(inputlist[2]),eval(inputlist[3]))),eval(inputlist[4]))
def Create_node(number=0,string='',dictionary={},list=[],nextprt=None):
    node = NODE(VALUE(number,string,dictionary,list),nextprt)
    return node
head = NODE(VALUE())
def In_stack():
    try:
        node = Create_node(*(Get_value()))
    except:
        print("OVERFLOW: No room availible!\n")
        exit(0)
    else:
        node.nextprt = head.nextprt
        head.nextprt = node
        return None
def Out_stack():
    if not head.nextprt:
        print("UNDERFLOW: The stack is empty!\n")
        return 0
    node = head.nextprt
    head.nextprt = node.nextprt
    return node.value
