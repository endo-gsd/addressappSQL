from abc import ABCMeta, abstractmethod


class MenuAbstract(metaclass=ABCMeta):
    @abstractmethod
    def execute_action(self, person_list):
        pass
