# varargs
def foo(*args, **kwargs):
  print("args", args)
  print("kwargs", kwargs)

foo("a", "b", "c", a="1", b="2", c="3")

# spreading
def boo(a, b, c):
  print(a, b, c)

boo(*("a", "b", "c"))
boo(**{"a": 1, "b": 2, "c": 3})
