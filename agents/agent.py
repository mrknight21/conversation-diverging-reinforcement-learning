from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, args):
        self.preprocessor = self.init_preprocessor(args)
        self.model = self.init_model(args)
        self.gpu = args.gpu

    @abstractmethod
    def batchify(self, batch, history):
        pass

    @abstractmethod
    def observe(self, batch ,history):
        pass

    @abstractmethod
    def respond(self, batch, history):
        pass

    @abstractmethod
    def init_model(self, arg):
        pass

