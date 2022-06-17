class singlylinkedlist:
  class node:
    def __init__(self,elemen,nextnode=None):
      self.element = elemen
      self.nextnode = nextnode
  def __init__(self):
    self.head = None
    self.size = 0
  def __str__(self):
    result=""
    pointer = self.head
    while pointer != None:
      result = result + str(pointer.element) + " "
      pointer = pointer.nextnode
    return result
  def addfirst(self,elemen):
    newnode = self.node(elemen)
    newnode.nextnode = self.head
    self.head = newnode
    self.size += 1
  def addlast(self,elemn):
    NewNode = self.node(elemn)
    if self.head == 0:
      self.head = NewNode
    else:
      pointer = self.head
      while pointer.nextnode != None:
        pointer = pointer.nextnode
      pointer.nextnode = NewNode
    self.size += 1
  def removefirst(self):
    if self.size > 0:
      if self.size == 1:
        self.head =None
        self.size -= 1
      else:
        pointer = self.head
        self.head = pointer.nextnode
        self.size -= 1
  def removelast(self):
    if self.size > 0:
      if self.size == 1:
        self.head =None
        self.size -= 1
      else:
        pointer = self.head
        while pointer.nextnode.nextnode != None:
          pointer = pointer.nextnode
        pointer.nextnode = None
        self.size -= 1
  def __len__(self):
    return self.size
def main(): 
  mylist = singlylinkedlist()
  mylist.addfirst(10)
  mylist.addlast(12)
  mylist.addfirst(9)
  mylist.addfirst(1)
  mylist.addfirst(3)
  mylist.addfirst(4)
  mylist.removefirst()
  mylist.removelast()
  mylist.removelast()
  print(str(mylist))
  
  print(len(mylist))
main()