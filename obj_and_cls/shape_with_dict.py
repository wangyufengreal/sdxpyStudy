import math


def get_square_perimeter(thing):
  return 4 * thing["side"]


def get_square_area(thing):
  return thing["side"] ** 2


def new_square_thing(name, side):
  return {
    "name": name,
    "side": side,
    "perimeter": get_square_perimeter,
    "area": get_square_area
  }


def get_circle_perimeter(thing):
  return 2 * math.pi * thing["radius"]


def get_circle_area(thing):
  return math.pi * (thing["radius"] ** 2)


def new_circle_thing(name, radius):
  return {
    "name": name,
    "radius": radius,
    "perimeter": get_circle_perimeter,
    "area": get_circle_area
  }


if __name__ == "__main__":
  things = [
    new_square_thing("sq", 3),
    new_circle_thing("ci", 2),
  ]

  for thing in things:
    n = thing["name"]
    p = thing["perimeter"](thing)
    a = thing["area"](thing)
    print(f"name: {n}, perimeter: {p:.2f}, area: {a:.2f}")
