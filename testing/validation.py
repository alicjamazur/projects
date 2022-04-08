

from abc import ABC, abstractmethod

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
       pass 

class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError('%r not a valid option. Shoud be one of %r' % (value, self.options))

class String(Validator):

    def __init__(self, minsize=0, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate
    
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        if len(value) < self.minsize:
            raise ValueError(f'String is too short, must be at least {self.minsize}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'String is too long, must be no bigger than {self.maxsize}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f'Expected {value} to be true for {self.predicate}')


class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue
    
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected an int or a float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Value {value} is too small, has to be bigger than {self.minvalue}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Value {value} is too big, has to be smaller than {self.maxvalue}')