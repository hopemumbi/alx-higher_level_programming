#!/usr/bin/python3

# STRINGS ARE IMMUTABLE
s = "abc"
identity_a = id(s)

# Assign new content to s
s = "xyz" # a new object is created instead of the contents being modified.
identity_b = id(s)

s += "uvw"
identity_c = id(s)

if identity_a == identity_b == identity_c:
    print("strings are mutable")
else:
    print("strings are immutable")

"""
Common immutable type:
 1. numbers: int(), float(), complex()
 2. immutable sequences: str(), tuple(), frozenset(), bytes()

Common mutable type (almost everything else):
 1.   mutable sequences: list(), bytearray()
 2.   set type: set()
 3.   mapping type: dict()
 4.   classes, class instances
"""
# INTEGERS ARE IMMUTABLE
i = 1
identity_i = id(i)

i += 1 # a new object is created instead of the contents being modified.
identity_j = id(i)

if identity_i == identity_j:
    print("integers are mutable")
else:
    print("integers are immutable")

# LISTS ARE MUTABLE
a = [1]
identity_l = id(a)

a.append(2) # The contents being modified but no new object is created instead
identity_k = id(a)
if identity_l == identity_k:
    print("lists are mutable")
else:
    print("lists are immutable")
print(type(a))
