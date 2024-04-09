#!/usr/bin/python3
# OBJECTS :  something a variable can refer to.

# STRINGS ARE IMMUTABLE
a = "banana"
b = "banana"
# `a` and `b` refer to the same string value and the same object.
#  `a` and `b` refer to two different things that have the same value

print(a == b) # Test whether `a` and `b` have the same value using `True`
print(a is b) # Test whether `a` and `b` refer to the same object `True`

# LISTS ARE MUTABLE
a = [1, 2, 3]
b = [1, 2, 3]

# `a` and `b` refer to the same list value but different objects.

print(a == b) # Test whether `a` and `b` have the same value `True`
print(a is b) # Test whether  `a` and `b` refer to the same object `False`

# LISTS: ALIASING
a = [1, 2, 3]
b = a
print(a is b) # Test whether  `a` and `b` refer to the same object `True`
# Since the same list has 2 diff names we  say it's aliased
# changes made with `b` affect `a` and viseversa
b[0] = 5
print(a)

# LISTS : CLONING - Use :
a = [1, 2, 3]
b = a[:]
print(b)
# changes made with `b` do not affect `a`
b[0] = 5
print(a)
