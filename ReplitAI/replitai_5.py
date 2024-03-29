"""
Canonical Solution:

def common(l1: list, l2: list) -> list:
  ret = set()
  for e1 in l1:
    for e2 in l2:
      if e1 == e2:
        ret.add(e1)
  return sorted(list(ret))

"""

# (Canonical Solution) Modify this function, so it returns unique elements that are not common for both lists in descending order.
def common(l1: list, l2: list) -> list:
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 != e2:
                ret.add(e1)
                ret.add(e2)
    return sorted(list(ret), reverse=True)

def check(candidate):

  assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [121, 34, 9, 7, 4, 3, 2]
  assert candidate([5, 3, 2, 8], [3, 2]) == [8, 5]
  assert candidate([4, 3, 2, 8], [3, 2, 4]) == [8]
  assert candidate([4, 3, 2, 8], [4, 3, 2, 8]) == []
  assert candidate([4, 3, 2, 8], []) == [8, 4, 3, 2]

check(common)


