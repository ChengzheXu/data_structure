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
def Create_liner_table(head):
    '''There must be sentence:
    head = NODE(VALUE())
    before you use this function to create a liner table.'''
    node = head
    while True:
        if int(input("If there is a postnode?(1 for Y,0 for N)\n")):
            try:
                node.nextprt = Create_node(*(Get_value()))
            except:
                print("OVERFLOW: No room availible.\n")
                exit(0)
            else:
                node = node.nextprt
        else:
            break
    return head
def Search_node_before_value(head,value):
    node = head
    target = None
    while node.nextprt:
        if node.nextprt.value == value:
            target = node
            break
        node = node.nextprt
    return target
def Add_node_after_value(head,value):
    target = (Search_node_before_value(head,value)).nextprt
    try:
        node = Create_node(*(Get_value()))
    except:
        print("OVERFLOW: No room availible.\n")
        exit(0)
    node.nextprt = target.nextprt
    target.nextprt = node
    return head
def Add_node_before_value(head,value):
    target = (Search_node_before_value(head,value))
    try:
        node = Create_node(*(Get_value()))
    except:
        print("OVERFLOW: No room availible.\n")
        exit(0)
    node.nextprt = target.nextprt
    target.nextprt = node
    return head
def Delete_node_after_value(head,value):
    target = (Search_node_before_value(head,value)).nextprt
    node = target.nextprt
    target.nextprt = node.nextprt
    return head
def Delete_node_before_value(head,value):
    target = (Search_node_before_value(head,value))
    node = target.nextprt
    target.nextprt = node.nextprt
    return head
def Array(head):
    if not head.nextprt or not head.nextprt.nextprt:
        return head
    unsorted = head.nextprt.nextprt
    head.nextprt.nextprt = None
    while unsorted:
        node = unsorted
        unsorted = node.nextprt
        sorted = head
        while sorted.nextprt:
            if sorted.nextprt.value >= node.value:
                target = sorted
                break
            sorted = sorted.nextprt
        node.nextprt = target.nextprt
        target.nextprt = node
    return head
def Array_reverse(head):
    if not head.nextprt or not head.nextprt.nextprt:
        return head
    unsorted = head.nextprt.nextprt
    head.nextprt.nextprt = None
    while unsorted:
        node = unsorted
        unsorted = node.nextprt
        sorted = head
        while sorted.nextprt:
            if sorted.nextprt.value <= node.value:
                target = sorted
                break
            sorted = sorted.nextprt
        node.nextprt = target.nextprt
        target.nextprt = node
    return head
