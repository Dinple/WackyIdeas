from abc import ABC, abstractmethod


class placeObj(ABC):
    def __init__(self, name, height, width):
        self.name_ = name
        self.height_ = height
        self.width_ = width
        # default location
        self.x_ = 0.0
        self.y_ = 0.0

    @abstractmethod
    def place(self, x, y):
        self.x_ = x
        self.y_ = y

    @abstractmethod
    def hash_color(self):
        pass

    @abstractmethod
    def dump(self):
        pass


class Macro(placeObj):
    def __init__(self, name, height, width):
        super().__init__(name, height, width)
        # default direction
        self.direction_ = "N"

    @classmethod
    def __init_with_direct__(cls, name, height, width, direction):
        cls(name, height, width)
        cls.direction = direction

    @property
    def name(self):
        return self.name_
    
    @property
    def direction(self):
        return self.direction_
    
    @name.setter
    def direction(self, value):
        self.direction_ = value

    def place(self, x, y):
        return super().place(x, y)
    
    def hash_color(self):
        return super().hash_color()

    def dump(self):
        print("[INFO] MACRO ==> (name:{}, height:{}, width:{}, x:{}, y:{})".format(
            self.name_, self.height_, self.width_, self.x_, self.y_))


class Netlist():
    pass