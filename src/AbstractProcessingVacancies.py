from abc import ABC, abstractmethod


class AbstractProcessingVacancies(ABC):
    @abstractmethod
    def insert(self, *args, **kwargs):
        pass

    @abstractmethod
    def search(self, *args, **kwargs):
        pass

    @abstractmethod
    def clear(self, *args, **kwargs):
        pass
