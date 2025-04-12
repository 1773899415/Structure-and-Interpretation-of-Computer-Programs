""" Homework 07: Special Method, Linked Lists and Mutable Trees"""

#####################
# Required Problems #
#####################



######################     单独一个空链表或只有一个数总是考虑不到，这样的话取rest或者branches就没用了，需要单独讨论，递归和循环都一样
#######################     要把最简单且符合题意的情况单独列出来讨论一下，每道题都是因为这个错
class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    def __init__(self,lst):
      self.lst=lst
      while self.lst[-1]==0 and len(self.lst)>1:
        self.lst.pop()
    def __repr__(self):
      return 'Polynomial({0})'.format(self.lst)
    def __str__(self):
      str1=''
      n=0
      for a in self.lst:
        if n==0:
          str1=str1+'{0}'.format(a)
        else:
          str1=str1+' + {0}*x^{1}'.format(a,n)
        n=n+1
      return str1
    def __add__(self,b):
      while b.lst[-1]==0 and len(b.lst)>1:
        b.lst.pop()
      k=min(len(self.lst),len(b.lst))
      i=0
      new_lst=[]
      while i<k:
        new_lst=new_lst+[self.lst[i]+b.lst[i]]
        i=i+1
      if len(self.lst)>len(b.lst):
        new_lst=new_lst+self.lst[k:]
      elif len(self.lst)<len(b.lst):
        new_lst=new_lst+b.lst[k:]
      return Polynomial(new_lst)
    def __mul__(self,b):
      new_lst1=[]
      i=1
      while b.lst[-1]==0 and len(b.lst)>1:
        b.lst.pop()
      for c in b.lst:
        new_lst1=new_lst1+[self.lst[0]*c]
      for a in range(len(self.lst)-1):
        new_lst1=new_lst1+[0]
      new_lst3=self.lst[1:]
      for a in new_lst3:
        new_lst2=[]
        for c in b.lst:
          new_lst2=new_lst2+[a*c]
        new_lst2=[0]*i+new_lst2+[0]*(len(new_lst3)-i)
        i=i+1
        for k in range(len(self.lst)+len(b.lst)-1):
          new_lst1[k]=new_lst1[k]+new_lst2[k]
      return Polynomial(new_lst1)


def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    if lnk is not Link.empty:
      if lnk.rest!=Link.empty:
        if lnk.first==lnk.rest.first:
          lnk.rest=lnk.rest.rest
          remove_duplicates(lnk)
        else:
          remove_duplicates(lnk.rest)


def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    a=lnk
    if a is Link.empty or a.rest is Link.empty:
      return a
    while a.rest!=Link.empty:
      a=a.rest
    if lnk.rest.rest!=Link.empty:########在函数体之前调用递归，本身就是对前面数据的一种存储
      reverse(lnk.rest)#################这种存储有利于先修改后面内容再修改前面内容
    if lnk.rest.rest==Link.empty:
      lnk.rest.rest=lnk
      lnk.rest=Link.empty
    return a
    


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self,tree0):
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        if self.is_leaf() and tree0.is_leaf() and self.label==tree0.label:
          return True
        elif not self.is_leaf() and not tree0.is_leaf() and self.label==tree0.label and len(self.branches)==len(tree0.branches):
          return all([Tree.__eq__(self.branches[i],tree0.branches[i]) for i in range(len(self.branches))])
        else:
          return False


def generate_paths(t, value):#找出一个树中所有的路径用nonlocal，每找到一个就在外面的list中保存一下，最后外面的list会装有所有的路径
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]
    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    s=[]
    k=[t.label]
    if t.is_leaf() and t.label==value:
      yield [t.label]
    def helper(t,value):
      nonlocal k
      nonlocal s
      l=k
      for a in t.branches:
        k=k+[a.label]
        if k[-1]==value:
          s=s+[k]
        helper(a,value)
        k=l
    helper(t,value)
    yield from s







def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    if total==0:
      return Tree('1')
    elif total<0:
      return None
    elif len(denominations)==0:
      return None
    without_current = count_coins_tree(total, denominations[1:])
    with_current = count_coins_tree(total - denominations[0], denominations)
    if without_current is not None and with_current is None:
      return Tree('{0}, {1}'.format(total,denominations),[without_current])
    elif without_current is None and with_current is not None:
      return Tree('{0}, {1}'.format(total,denominations),[with_current])
    elif without_current is not None and with_current is not None:
      return Tree('{0}, {1}'.format(total,denominations),[without_current,with_current])


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def bst_max(a):
      if len(a.branches)==2:
        return max(a.branches[0].label,a.branches[1].label)
      elif len(a.branches)==1:
        return a.branches[0].label
    def bst_min(a):
      if len(a.branches)==2:
        return min(a.branches[0].label,a.branches[1].label)
      elif len(a.branches)==1:
        return a.branches[0].label
    if t.is_leaf():
      return True
    elif len(t.branches)>2:
      return False
    elif len(t.branches)==2:
      if t.branches[0].label>t.label or t.branches[1].label<=t.label:
        return False
    for a in t.branches:
      if a.label<=t.label:
        if len(a.branches)>=1 and len(a.branches)<=2:
          if bst_max(a)>t.label:
            return False
        elif len(a.branches)>2:
          return False
      elif a.label>t.label:
        if len(a.branches)>=1 and len(a.branches)<=2:
          if bst_min(a)<=t.label:
            return False
          elif len(a.branches)>2:
            return False
    return all([is_bst(k) for k in t.branches])##这种list-comprehension用得太多了 all any非常好用 尤其是递归
    


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'



def helper1(t):#preorder
      str0=[t.label]
      for a in t.branches:
        str0=str0+helper1(a)
      return str0


def f(t):#可以生成Tree的所有路径  生成Tree的所有路径用nonlocal  定义helper函数  保存当前list然后递归调用helper 再让用的list变回当前list
  s=[[t.label]]
  k=[t.label]
  def helper(p):
    nonlocal k
    nonlocal s
    q=[p.label]
    l=k
    for a in p.branches:
      k=k+[a.label]
      s=s+[k]
      helper(a)
      k=l
  helper(t)
  return s

def map1(lnk,func):
  if lnk is not Link.empty:
    lnk1=Link(func(lnk.first),map1(lnk.rest,func))
  elif lnk is Link.empty:
    return lnk
  return lnk1

def map2(tree0,func):
  if tree0.is_leaf():
    tree0.label=func(tree0.label)
  else:
    tree0.label=func(tree0.label)
    for branch in tree0.branches:
      map2(branch,func)


def storedigit(n):
  lnk=Link.empty
  if n==0:
    return Link(0)
  while n>0:
    lnk=Link(n%10,lnk)
    n=n//10
  return lnk

def cumulative(tree0):
  for branch in tree0.branches:
    if not branch.is_leaf():
      cumulative(branch)
    tree0.label=tree0.label+branch.label

def reverse1(lnk):
  if lnk is Link.empty or lnk.rest is Link.empty:
    return lnk
  p1=lnk
  p2=lnk.rest
  tail=lnk
  while tail.rest is not Link.empty:
    tail=tail.rest
  p1.rest=Link.empty
  if p2.rest is not Link.empty:
    reverse1(p2)
  p2.rest=p1
  return tail

def generate(t,value):
  lst=[]
  def helper(t,value):
    nonlocal lst
    lst2=[]
    lst2.append(t.label)
    if t.label==value:
      lst.append(lst2)

  helper(t,value)
  yield from lst
