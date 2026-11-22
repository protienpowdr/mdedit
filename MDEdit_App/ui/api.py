from enum import Enum, auto
from collections.abc import Callable
from typing import Any

class AppWidgetType(Enum):
    pass

class AppInterface(Enum):
    ChangeAppTheme = auto()


class AppFunctionResolver:

    def __init__(self):
        self.reg: dict[AppInterface,Callable[...,Any]] = {}

    def add_entry(self, key,value):
        self.reg.update({key : value})

    def get_entry(self,key):
        return self.reg.get(key)


class AppWidgetResolver:

    def __init__(self):
        self.reg : dict[AppWidgetType,Callable[...,Any]] = {}

    def add_entry(self, key,value):
        self.reg.update({key : value})

    def get_entry(self,key):
        return self.reg.get(key)
