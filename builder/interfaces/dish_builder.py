from abc import ABC, abstractmethod, abstractproperty

class IDishBuilder(ABC):

    @abstractproperty
    def dish(self):
        pass

    @abstractmethod
    def cook_rice(self):
        pass