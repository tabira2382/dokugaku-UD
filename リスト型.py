# bikyo@tabiratuhinoMBP dokugaku-UD % python
#
# WARNING: Python 2.7 is not recommended.
# This version is included in macOS for compatibility with legacy software.
# Future versions of macOS will not include Python 2.7.
# Instead, it is recommended that you transition to using 'python3' from within Terminal.
#
# Python 2.7.16 (default, Jun  5 2020, 22:59:21)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> l = [1,20,4,50,2,1,2]
# >>>
# >>> l
# [1, 20, 4, 50, 2, 1, 2]
# >>> l[0]
# 1
# >>> l[1]
# 20
# >>> l[-1]
# 2
# >>> l[-2]
# 1
# >>> l[:2]
# [1, 20]
# >>> l[2:5]
# [4, 50, 2]
# >>> l[2:]
# [4, 50, 2, 1, 2]
# >>> l[:]
# [1, 20, 4, 50, 2, 1, 2]
# >>> len(l)
# 7
# >>> type(l)
# <type 'list'>
# >>> list('abcdefg')
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> l[100]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> n = [1,2,,3,4,5,6,7,8,9,10]
#   File "<stdin>", line 1
#     n = [1,2,,3,4,5,6,7,8,9,10]
#              ^
# SyntaxError: invalid syntax
# >>> n = [1,2,3,4,5,6,7,8,9,10]
# >>> n[::2]
# [1, 3, 5, 7, 9]
# >>> n[::-1]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# >>> a = ['a','b','c']
# >>> n = [1,2,3]
# >>> x = [a,n]
# >>> x
# [['a', 'b', 'c'], [1, 2, 3]]
# >>> x[0]
# ['a', 'b', 'c']
# >>> x[1]
# [1, 2, 3]
# >>> x[0][1]
# 'b'
# >>> x[1][3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> x[1][2]
# 3
