from types import MethodType


class Decorator(object):

    def __init__(self, func, name, files):
        self.func = func
        self.name = name
        self.files = files

    def __call__(self, *args, **kwargs):
        def read_and_join_csv():
            with open(self.files, 'r') as f:
                return ''.join(f.readlines())
        return self.func(*args, **kwargs)


    # def __get__(self, instance, cls):
    #     # Retorna un método si se llama en una instancia
    #     print(MethodType(self, instance))
    #     return self if instance is None else MethodType(self, instance)
