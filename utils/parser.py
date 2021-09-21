from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_data(self,filename1, filename2=None):
        pass

    