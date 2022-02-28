import json, os
from argparse import ArgumentParser
from datasets.dataset_preprocessor import DatasetPreprocessor;


class DailyDialoguePreprocessor(DatasetPreprocessor):

    def __init__(self):
        super(DailyDialoguePreprocessor, self).__init__("dailydialogue")

    def process_single_dialogue(self, dialogue):
        processed_dialogue = {
            "metadata": {
                'type': dialogue['fold'],
                'topic': dialogue['topic']
            },
            'dialogue': []
        }
        for idx, utterance in enumerate(dialogue['dialogue']):
            processed_dialogue['dialogue'].append(self.process_single_utterance(utterance, idx))
        return processed_dialogue

    def process_single_utterance(self, utterance, index):
        processed_utterance = {
            "text": utterance['text'],
            "labels": {
                "emotion": utterance['emotion'],
                "act": utterance['act']
            },
            "index": index
        }
        return processed_utterance

    def process_whole_dataset(self, input_folder, output_folder):
        for data_type in ["valid", "train", "test"]:
            data = []
            for line in open(input_folder + "/" + data_type + ".json", 'r'):
                json_obj = self.process_single_dialogue(json.loads(line))
                data.append(json_obj)
            with open(output_folder + "/" + self.name + "_" + data_type + '.json', 'w') as f:
                json.dump(data, f)
        return


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--verbose', action='store_true', help='print individual scores')
    parser.add_argument('--output_folder', type=str, required=True, help='Path to dataset output.')
    parser.add_argument('--input_folder', type=str, required=True, help='Path to raw dataset input.')
    args = parser.parse_args()
    print(os.getcwd())
    processor = DailyDialoguePreprocessor()
    processor.process_whole_dataset(args.input_folder, args.output_folder)
