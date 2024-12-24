import math

### Shape ###

def shape_density(thing, weight):
  return weight / call(thing, "area")


def new_shape_thing(name):
  return {
    "name": name,
    "_class": Shape
  }


Shape = {
  "_classname": "shape",
  "density": shape_density,
  "_parent": None,
  "_new": new_shape_thing
}


### Square ###

def get_square_perimeter(thing):
  return 4 * thing["side"]


def get_square_area(thing):
  return thing["side"] ** 2


def is_square_larger(thing, size):
  return call(thing, "area") > size


def new_square_thing(name, side):
  return make(Shape, name) | {
    "side": side,
    "_class": Square,
  }


Square = {
  "_classname": "square",
  "larger": is_square_larger,
  "perimeter": get_square_perimeter,
  "area": get_square_area,
  "_parent": Shape,
  "_new": new_square_thing,
}


### Circle ###


def get_circle_perimeter(thing):
  return 2 * math.pi * thing["radius"]


def get_circle_area(thing):
  return math.pi * (thing["radius"] ** 2)


def is_circle_larger(thing, size):
  return call(thing, "area") > size


def new_circle_thing(name, radius):
  return make(Shape, name) | {
    "radius": radius,
    "_class": Circle,
  }


Circle = {
  "_classname": "circle",
  "larger": is_circle_larger,
  "perimeter": get_circle_perimeter,
  "area": get_circle_area,
  "_parent": Shape,
  "_new": new_circle_thing,
}


### Function call tool ###


def call(thing, method_name, *args):
  method = find(thing['_class'], method_name)
  return method(thing, *args)


def find(_cls, method_name):
  while _cls is not None:
    if method_name in _cls:
      return _cls[method_name]
    _cls = _cls["_parent"]
  raise NotImplementedError(f"method_name: {method_name}")


### Make tool ###


def make(_cls, *args):
    return _cls["_new"](*args)


if __name__ == "__main__":
  things = [
    make(Square, "sq", 3),
    make(Circle, "ci", 2),
  ]

  for thing in things:
    n = thing["name"]
    d = call(thing, "density", 10)
    print(f"name: {n}, which weight is 10, density is: {d:.2f}")
