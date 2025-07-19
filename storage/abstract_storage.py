from abc import ABC, abstractmethod

class AbstractStorage(ABC):
    @abstractmethod
    def save(self):
        pass
    def load(self):
        pass
    def delete(self):
        pass
