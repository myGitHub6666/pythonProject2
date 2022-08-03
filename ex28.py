"""
In [1]: True and True
Out[1]: True

In [2]: False and True
Out[2]: False

In [3]: 1 == 1 and 2 ==1
Out[3]: False

In [4]: "test" == "test"
Out[4]: True

In [5]: 1 == 1 or 2 != 1
Out[5]: True

In [6]: True and 1 ==1
Out[6]: True

In [7]: "test" == "testing"
Out[7]: False

In [8]: 1 != 0 and 2 ==1
Out[8]: False

In [9]: "test" != "testing"
Out[9]: True

In [10]: "test
  Input In [10]
    "test
    ^
SyntaxError: unterminated string literal (detected at line 1)


In [11]: "test" == 1
Out[11]: False

In [12]: not ( True and False )
Out[12]: True

In [13]: not ( 1 == 1 and 0 != 1)
Out[13]: False

In [14]: not ( 10 == 1 or 1000 == 1000)
Out[14]: False

In [15]: not ( 1 != 10 or 3 == 4)
Out[15]: False

In [16]: not ( "testing" == "testing" and "Zed" == "Cool Guy")
Out[16]: True

In [17]: 1 == 1 and not ("testing" == 1 or 1 == 0)
Out[17]: True

In [18]: "chunky" == "bacon" and not (3==4 or 3==3)
Out[18]: False

In [19]: 3 == 3 and not ("testiong" == "testing" or "Python" == "Fun")
Out[19]: True

In [20]: 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
Out[20]: False """
