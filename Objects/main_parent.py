from abc import ABC, abstractmethod

class main_parent(ABC):

    @abstractmethod
    def main_run(self):
        pass

    @abstractmethod
    def gui_out(self):
        pass