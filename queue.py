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
tail = NODE(VALUE())
head = NODE(VALUE())
def Get_value():
    inputlist = input('''Please enter the value of node.
    (Format:number-string-the key of dictionary-the value of dictionary-the list)\n''').split('-')
    return (eval(inputlist[0]),inputlist[1],dict(zip(eval(inputlist[2]),eval(inputlist[3]))),eval(inputlist[4]))
def Create_node(number=0,string='',dictionary={},list=[],nextprt=None):
    node = NODE(VALUE(number,string,dictionary,list),nextprt)
    return node
def In_queue():
    try:
        node = Create_node(*(Get_value()))
    except:
        print("OVERFLOW: No room availible!\n")
        exit(0)
    if not head.nextprt or not tail.nextprt:
        tail.nextprt = head.nextprt = node
    else:
        tail.nextprt = node
        tail = node
    return None
def Out_queue():
    if head.nextprt == tail.nextprt:
        if not head.nextprt:
            print("UNDERFLOW: the queue is empty!\n")
            exit(0)
        else:
            node = head.nextprt
            head.nextprt = tail.nextprt = None
            return node.value
    else:
        node = head.nextprt
        head.nextprt = node.nextprt
        return node.value
