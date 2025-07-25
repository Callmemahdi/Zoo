from abc import ABC, abstractmethod

class AbstractStorage(ABC):
    @abstractmethod
    def save(self, animal):
        pass
    def load(self):
        pass
    @abstractmethod
    def delete(self, unique_id):
        pass

