# 11. Write a Python program to use of frozensets.

class FrozenSet:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._dict = {item: None for item in iterable}

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __str__(self):
        return "FrozenSet(" + str(list(self._dict.keys())) + ")"

def create_frozenset():
    my_set = {1, 2, 3, 4, 5}
    frozen_set = FrozenSet(my_set)
    print("Frozen set:", frozen_set)

create_frozenset()
