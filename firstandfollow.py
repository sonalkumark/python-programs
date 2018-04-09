class ff:
  prod={}
  terminals=[]
  first={}
  follow={}
  def listtostr(self,c):
    temp=""
    for i in c:
      temp=temp+i
    return temp
  def strtolist(self,c):
    temp=[]
    for i in c:
      temp.append(i)
    return temp
  
  def union(self,f,s):
    temp=[]
    f=self.strtolist(f);
    s=self.strtolist(s);
    for i in f:
      if i not in temp:
        temp.append(i)
    for i in s:
      if i not in temp:
        temp.append(i)
    return temp
    
  def strwonull(self,l):
    l=self.strtolist(l)
    l=l.remove('^')
    l=self.listtostr(l)
    return l
    
  def find_follow(self,entry):
    temp=self.prod[entry].split('|')
    sdf=""
    nt=""
    z=""
    for i in temp:
      if i.__contains__(entry):
        try:
          if self.isTerminal(i[i.index(entry)+1]):
            sdf=sdf+i[i.index(entry)+1]
          elif self.isNonTerminal(i[i.index(entry)+1]):
            try:
              z=self.strwonull(self.first[i[i.index(entry)+1]])
              if self.follow[i[i.index(entry)+1]]!='':
                z=z+self.follow[i[i.index(entry)+1]]
              else:
                z=z+self.find_follow(i[i.index(entry)+1])
            except:
              z=z+self.find_follow(self.prod[entry])
            sdf=z
        except:
          z=z+self.find_follow(self.prod[entry])
        sdf=z  
    return sdf;
    
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
      for i in self.prod:
        self.follow[i]=self.find_follow(i)
      print "follow table is"
      for i in self.first:
        print i+" "+self.follow[i]
    
    
obj=ff()
obj.main()
