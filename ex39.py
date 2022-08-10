#
# In [1]: thing = ['a', 'b', 'c']
#
# In [2]: print(thing[1])
# b
#
# In [3]: thing[1] = 'b'
#
# In [4]: print(thing[1])
# b
#
# In [5]: things
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Input In [5], in <cell line: 1>()
# ----> 1 things
#
# NameError: name 'things' is not defined
#
# In [6]: thing
# Out[6]: ['a', 'b', 'c']
#
# In [7]: print(thing)
# ['a', 'b', 'c']
#
# In [8]: stuff ={'name':'zed', 'age':39, 'height':6*12+2}
#
# In [9]: print(stuff['name'])
# zed
#
# In [10]: print(stuff['age'])
# 39
#
# In [11]: print(stuff['height'])
# 74
#
# In [12]: stuff['city'] = "SF"
#
# In [13]: prin(stuf['city'])
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Input In [13], in <cell line: 1>()
# ----> 1 prin(stuf['city'])
#
# NameError: name 'prin' is not defined
#
# In [14]: prin(stuff['city'])
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# Input In [14], in <cell line: 1>()
# ----> 1 prin(stuff['city'])
#
# NameError: name 'prin' is not defined
#
# In [15]: print(stuff['city'])
# SF
#
# In [16]: print(stuff)
# {'name': 'zed', 'age': 39, 'height': 74, 'city': 'SF'}
#
# In [17]:
stuff = [1, 3, 4, 5]
print(stuff[0])
print(stuff[1])
stuff[1] = 4
print(stuff[1])
print(stuff)

stuff1 = {'name': 'xiaoxin', 'age': 3, 'height': 105}
print(stuff1['name'])
stuff1['name'] = 'pipi'
stuff1['city'] ="xi'an"
print(stuff1)
