class ff:
  prod={}
  terminals=[]
  first={}
  def isTerminal(self,c):
    if c in self.terminals:
      return True
    else:
      return False
  def isNULL(self,c):
    if c=='^':
      return True
    else:
      return False
  def isNonTerminal(self,c):
    if c not in self.terminals:
      if c!='^':
        return True
    else:
      return False
  def find_first(self,entry):
    temp=self.prod[entry].split('|')
    sdf=""
    nt=""
    for i in temp:
      if self.isTerminal(i[0]):
        sdf=sdf+i[0]
      elif self.isNULL(i[0]):
        sdf=sdf+i[0]
      elif self.isNonTerminal(i[0]):
        sdf=sdf+(self.find_first(i[0]))
    print "sdf is "+sdf
    return sdf;
  def main(self):
      n=int(input("Enter number of productions:"))
      for i in range(0,n):
        temp=raw_input("Enter production:")
        temp=temp.split("->")
        self.prod[temp[0]]=temp[1]
      temp=raw_input("enter terminals with , separated:")
      self.terminals=temp.split(",")
      for i in self.prod:
        self.first[i]=self.find_first(i)
      print "first table is"
      for i in self.first:
        print i+" "+self.first[i]

    
    
obj=ff()
obj.main()
