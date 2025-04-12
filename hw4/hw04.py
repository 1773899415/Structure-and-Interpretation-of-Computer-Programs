""" Homework 4: Data Abstraction and Trees"""

from math import sqrt
from ADT import is_tree, make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    lst = lst1 + lst2
    return [[lst1[x], lst[x + len(lst1)]] for x in range(len(lst1))]



def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    a=get_lat(city1)
    b=get_lat(city2)
    c=get_lon(city1)
    d=get_lon(city2)
    return sqrt((a-b)**2+(c-d)**2)


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    city3=make_city('liyuhan',lat,lon)
    if distance(city1, city3)<distance(city2, city3):
      return get_name(city1)
    elif distance(city1, city3)>distance(city2, city3):
      return get_name(city2)


def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    if label(t)=='nut':
      return True
    else:
      k,i=0,0
      a=False
      for b in branches(t):
        k=k+1
      while i<k:
        a=a or nut_finder(branches(t)[i])
        i=i+1
    return a


def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
      return tree(label(t),[tree(a) for a in values])
    elif is_tree(t):
      return tree(label(t),[sprout_leaves(a,values) for a in branches(t)])

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), 
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
      return tree(label(t1)+label(t2))
    elif is_leaf(t1) and is_tree(t2):
      return tree(label(t1)+label(t2),branches(t2))
    elif is_tree(t1) and is_leaf(t1):
      return tree(label(t1)+label(t2),branches(t1))
    else:
      t11=branches(t1)
      t22=branches(t2)
      longest=min(len(t11),len(t22))
      v=[add_trees(t11[i],t22[i]) for i in range(longest)]
      if len(t11)>len(t22):
        c=[t11[len(t22)+l] for l in range(len(t11)-len(t22))]
        return tree(label(t1)+label(t2),v+c)
      elif len(t11)<len(t22):
        c=[t22[len(t11)+l] for l in range(len(t22)-len(t11))]
        return tree(label(t1)+label(t2),v+c)
      else:
        return tree(label(t1)+label(t2),[add_trees(t11[i],t22[i])for i in range(longest)])
def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    a=0
    if label(t)>=n:
      a=a+1
    k,i=0,0
    for b in branches(t):
      k=k+1
    while i<k:
      a=a+bigpath(tree(label(t)+label(branches(t)[i]),branches(branches(t)[i])),n)
      i=i+1
    return a
      

def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    k,i=0,0
    a=0
    for b in branches(t):
      k=k+1
    while i<k:
      a=a+bigger_path(branches(t)[i],n)
      i=i+1
    return bigpath(t,n)+a

##########################
# Just for fun Questions #
##########################


def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"


def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def reverse(t):
  if is_leaf(t):
    return tree(label(t))
  else:
    reversed_branches=[branches(t)[len(branches(t))-i-1] for i in range(len(branches(t)))]
    return tree(label(t),[reverse(k) for k in reversed_branches])

def equals_tree(t1, t2):
  return label(t1) == label(t2) and \
    all([any([equals_tree(b1, b2) for b2 in branches(t2)]) for b1 in branches(t1)])

def f(a,b):
  if is_leaf(a):
    return b+[label(a)]
  else:
    b=b+[label[a]]
    return [b]+[f(x,b) for x in branches(a)]