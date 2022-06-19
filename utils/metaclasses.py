class Singleton(type):
    __instances = {}

    def __call__(self, *args, **kwargs):

        if self not in self.__instances:
            instance = super().__call__(*args, **kwargs)
            self.__instances[self] = instance
        return self.__instances[self]
