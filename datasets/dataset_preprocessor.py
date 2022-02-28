
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class DatasetPreprocessor(ABC):

    def __init__(self, name):
        self.name = name

    def processing_single_dialogue(self, dialogue):
        return dialogue

    def processing_single_utterance(self, utterance):
        return utterance

    def processing_whole_dataset(self, input_folder, output_folder):
        return

