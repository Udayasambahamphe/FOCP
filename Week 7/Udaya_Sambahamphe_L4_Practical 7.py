#1
names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print(names)


#2
sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence}


#3
names = {"John", "Jane", "Sam", "Jill"}

name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names")
else:
    print("You are listed in the set of known names")

#4
help(set)

#5
staff = {"Paul", "John", "George"}
directors = {"Michael", "Sir George Martin"}

staff = staff.union({"Mark", "Ringo"})
print(staff)

inter_section= staff.intersection(directors)
print(inter_section)

diff_erence = staff.difference(directors)
print(diff_erence)

sym_difference = staff.symmetric_difference(directors)
print(sym_difference)

#6
vowels = set({"a", "e", "i"})
vowels.update({"o", "u"})
print(vowels)

#7
staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("All managers are staff members")

#8
help(frozenset)

# class frozenset(object)
#  |  frozenset() -> empty frozenset object
#  |  frozenset(iterable) -> frozenset object
#  |
#  |  Build an immutable unordered collection of unique elements.
#  |
#  |  Methods defined here:
#  |
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |
#  |  __contains__(...)
#  |      x.__contains__(y) <==> y in x.
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)

#9
import math
roots = {n : math.sqrt(n) for n in range(1,26)}
print(roots)

#10
stock = {'apple': 1, 'banana': 4, 'cherry': 9}
stock['kiwi'] = 10
print(stock)

#11
help(dict)
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).

stock = {'apple': 1, 'banana': 4, 'cherry': 9, 'kiwi': 10}
popped_items = stock.popitem() 
print(popped_items)
print(stock)

#12
roots = {4: 2, 9: 3, 16: 4, 25: 5}
for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")

#13
Set: An unordered collection of unique elements.
Set Operations: Manipulations like union, intersection, and difference on sets.
Set Comprehension: Creating sets using a concise and expressive syntax based on a condition.
Dictionary: A collection of key:value pairs, providing an efficient way to store and retrieve data.
Key:Value Pair: The fundamental components of a dictionary, where