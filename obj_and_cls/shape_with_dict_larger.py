import math


def get_square_perimeter(thing):
  return 4 * thing["side"]


def get_square_area(thing):
  return thing["side"] ** 2


def is_square_larger(thing, size):
  return call(thing, "area") > size


Square = {
  "_classname": "square",
  "larger": is_square_larger,
  "perimeter": get_square_perimeter,
  "area": get_square_area,
}


def new_square_thing(name, side):
  return {
    "name": name,
    "side": side,
    "_class": Square,
  }


def get_circle_perimeter(thing):
  return 2 * math.pi * thing["radius"]


def get_circle_area(thing):
  return math.pi * (thing["radius"] ** 2)


def is_circle_larger(thing, size):
  return call(thing, "area") > size


Circle = {
  "_classname": "circle",
  "larger": is_circle_larger,
  "perimeter": get_circle_perimeter,
  "area": get_circle_area,
}


def new_circle_thing(name, radius):
  return {
    "name": name,
    "radius": radius,
    "_class": Circle,
  }


def call(thing, method_name, *args):
  return thing["_class"][method_name](thing, *args)


if __name__ == "__main__":
  things = [
    new_square_thing("sq", 3),
    new_circle_thing("ci", 2),
  ]

  for thing in things:
    n = thing["name"]
    cn = thing["_class"]["_classname"]
    p = call(thing, "perimeter")
    a = call(thing, "area")
    print(f"name: {n}, class name: {cn}, perimeter: {p:.2f}, area: {a:.2f}")
    result = call(thing, "larger", 10)
    print(f"Is size larger than 10? {result}")
