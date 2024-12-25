## Multiple inheritance

* origin python method look up order: get all method, use C3 algorithm to sort them.

* prompt: 帮我设计一个算法，[
  in python, i have a dict_a, it look like {
    "f1": 0,
    "_parent": [dict_b, dict_c]
  }, _parent key is his father, shape like dict_a. and i want find all dict's key name, like "f1". and i don't know dict_n's parent number and quantity, please design a general purpose alogrithm.
]

## Class method and static method

* Class method: method which need class as implicit parameter.
* Static method: only use class as a way of orgnization, use it as normal function.

## type() and isinstance() method

* type(): get type.
* isinstance(x, y): find all of x's related classes, and judge is y in these guys?

* fake_isinstance design: 

1. for isinstance: it must have "_class" field. and this is the first type i need judge.
2. i need judge all of the first class's parent class, is the type suitable for the input.
