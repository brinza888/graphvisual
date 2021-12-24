from collections import defaultdict
from abc import ABCMeta, abstractmethod


def check_selectable_decorator(func):
    def wrapped(self, obj, *args, **kwargs):
        if not isinstance(obj, Selectable):
            raise TypeError("Passed object must be Selectable")
        return func(self, obj, *args, **kwargs)
    return wrapped


class SelectionManager:
    def __init__(self):
        self.selected = defaultdict(list)

    @check_selectable_decorator
    def select(self, obj):
        self.selected[obj.selection_id].append(obj)

    def clear(self, cls):
        selection_id = SelectionManager.selection_id_by_cls(cls)
        self.selected[selection_id].clear()

    def fetch_one(self, cls):
        selection_id = SelectionManager.selection_id_by_cls(cls)
        if not self.selected[selection_id]:
            return None
        return self.selected[selection_id].pop()

    def fetch_all(self, cls):
        selection_id = SelectionManager.selection_id_by_cls(cls)
        return self.selected[selection_id].copy()

    @staticmethod
    def selection_id_by_cls(cls):
        if not isinstance(cls, type):
            raise TypeError("Passed object must be a type-object")
        return cls.__name__


class Selectable (metaclass=ABCMeta):
    def __init__(self):
        self.__selected = False

    @property
    def selected(self):
        return self.__selected

    @classmethod
    @property
    def selection_id(cls):
        return cls.__name__

    def select(self):
        self.__selected = True

    def deselect(self):
        self.__selected = False


class A (Selectable):
    def __init__(self, x, y):
        super(A, self).__init__()
        self.x, self.y = x, y


sm = SelectionManager()

ex_a = A(10, 20)
ex_a2 = A(20, 10)

sm.select(ex_a)

print(sm.selected.items())

print(sm.fetch_all(A))
