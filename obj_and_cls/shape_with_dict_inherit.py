import math


### Magic ###
# This is a world make up of sword and magic ~
# Every thing have its magic.


def new_magic_thing(attribute, strength):
  return {
    "attribute": attribute,
    "strength": strength,
  }


def damage(thing):
  return f"{thing['attribute']}*{thing['strength']:.1f}"


def classmethod_get_environment_magic_density(_cls):
  return _cls["environment_magic_density"]


def staticmethod_damage_gain(damage, gain_coeff):
  return damage * gain_coeff


Magic = {
  "_classname": "magic",
  "_parent": None,
  "damage": damage,
  "classmethod_get_environment_magic_density": classmethod_get_environment_magic_density,
  "environment_magic_density": 666.66,
  "staticmethod_damage_gain": staticmethod_damage_gain,
  "_new": new_magic_thing
}


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


def new_square_thing(name, side, attribute, strength):
  return make(Shape, name) | make(Magic, attribute, strength) | {
    "side": side,
    "_class": Square,
  }


Square = {
  "_classname": "square",
  "larger": is_square_larger,
  "perimeter": get_square_perimeter,
  "area": get_square_area,
  "_parent": [Shape, Magic],
  "_new": new_square_thing,
}


### Circle ###


def get_circle_perimeter(thing):
  return 2 * math.pi * thing["radius"]


def get_circle_area(thing):
  return math.pi * (thing["radius"] ** 2)


def is_circle_larger(thing, size):
  return call(thing, "area") > size


def new_circle_thing(name, radius, attribute, strength):
  return make(Shape, name) | make(Magic, attribute, strength) | {
    "radius": radius,
    "_class": Circle,
  }


Circle = {
  "_classname": "circle",
  "larger": is_circle_larger,
  "perimeter": get_circle_perimeter,
  "area": get_circle_area,
  "_parent": [Shape, Magic],
  "_new": new_circle_thing,
}


### Function call tool ###


def call(thing, method_name, *args, **kwargs):
  # Parameters check
  if not isinstance(thing, dict):
    raise ValueError("thing must be dict type!")

  if method_name.startswith("staticmethod"):
    return thing[method_name](*args, **kwargs)
  elif method_name.startswith("classmethod"):
    # class method process
    return thing[method_name](thing, *args, **kwargs)
  else:
    # object instance function process
    method = find(thing['_class'], method_name)
    if method is None:
      raise ValueError("You call a method i can't find!")
    return method(thing, *args, **kwargs)
  

def find(_cls, method_name, seen=None):

  # Parameters check
  if not isinstance(_cls, dict):
    raise ValueError("class is not dict type!")
  if not isinstance(method_name, str):
    raise ValueError("method name is not str type!")

  if seen is None:
    seen = set()
  
  cls_id = id(_cls)
  if cls_id in seen:
    return None
  seen.add(cls_id)

  # Is the method i want in this class?
  if method_name in _cls.keys():
    return _cls[method_name]
  
  # Is this class have parent class?
  if "_parent" in _cls.keys():
    if isinstance(_cls["_parent"], list):
      for p_cls in _cls["_parent"]:
        res = find(p_cls, method_name, seen)
        if res is not None:
          return res
    if isinstance(_cls["_parent"], dict):
      res = find(_cls["_parent"], method_name, seen)
      if res is not None:
        return res
      
  return None



### Make tool ###


def make(_cls, *args, **kwargs):
    return _cls["_new"](*args, **kwargs)


if __name__ == "__main__":
  things = [
    make(Square, "sq", side=3, attribute="ice", strength=5),
    make(Circle, "ci", radius=2, attribute="fire", strength=8),
  ]

  for thing in things:
    n = thing["name"]
    d = call(thing, "damage")

    print(f"name: {n} -> cause damage: {d}")

  e = call(Magic, "classmethod_get_environment_magic_density")
  print(f"environment magic density: {e}")

  gd = call(Magic, "staticmethod_damage_gain", 8, 2.0)
  print(f"gained damage is: {gd}")
