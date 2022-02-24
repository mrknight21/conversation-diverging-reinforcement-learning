import json
import logging
import msgpack

log = logging.getLogger(__name__)


class QuacGeneralProcessor:

    def __init__(self, args):
        self.train_file = args.train_file
        self.dev_file = args.dev_file
        self.save_train_file = args.save_train_file
        self.save_dev_file = args.save_dev_file
        self.args = args

    def run(self):
        train_raw_data = self.load_raw_data(self.train_file)
        if train_raw_data:
            log.info('loaded quac train data')
            quac_train_data = self.dialogues_unpack(train_raw_data)
            if self.msgpack_dump(quac_train_data, self.save_train_file):
                del train_raw_data
                del quac_train_data
                log.info('saved quac preprocessed train data')
            else:
                log.info('failed saving quac preprocessed train data')
        else:
            log.info('failed loading quac train data')

        dev_raw_data = self.load_raw_data(self.dev_file)
        if dev_raw_data:
            log.info('loaded quac dev data')
            quac_dev_data = self.dialogues_unpack(dev_raw_data)
            if self.msgpack_dump(quac_dev_data, self.save_dev_file):
                del dev_raw_data
                del quac_dev_data
                log.info('saved quac preprocessed dev data')
        else:
            log.info('failed loading quac dev data')


    def load_raw_data(self, file):
        with open(file, encoding="utf8") as f:
            data = json.load(f)['data']
            return data
        return None


    def msgpack_dump(self, json, file):
        with open(file, 'wb') as f:
            msgpack.dump(json, f)
            return True
        return False


    def dialogues_unpack(self, data):
        quac_data = []
        for conv in data:
            dialogue = []
            dialogue_json = {
                "title": conv['title'],
                "background": conv['background'],
                "section_title": conv['section_title'],
                "context": conv["paragraphs"][0]['context'],
                "id": conv["paragraphs"][0]['id']
            }
            for qa in conv["paragraphs"][0]['qas']:
                question = qa['question']
                answers = qa['orig_answer']

                answer = answers['text']
                answer_start = answers['answer_start']
                answer_end = answers['answer_start'] + len(answers['text'])
                answer_choice = 0 if answer == 'CANNOTANSWER' else \
                    1 if qa['yesno'] == 'y' else \
                        2 if qa['yesno'] == 'n' else \
                            3  # Not a yes/no question
                """
                0: Do not ask a follow up question!
                1: Definitely ask a follow up question!
                2: Not too important, but you can ask a follow up.
                """
                answer_followup = 0
                if qa['followup'] == "n":
                    answer_followup = 0
                elif qa['followup'] == "y":
                    answer_followup = 1
                else:
                    answer_followup = 2
                if answer_choice == 0:
                    answer_start, answer_end = -1, -1
                ans_ls = []
                for ans in qa['answers']:
                    ans_ls.append(ans['text'])
                qa_pair = {
                    "question": question,
                    "answer": answer,
                    "answer_start": answer_start,
                    "answer_end": answer_end,
                    "answer_choice": answer_choice,
                    "answer_followup": answer_followup,
                    "ans_ls": ans_ls
                }
                dialogue.append(qa_pair)
            dialogue_json['dialogue'] = dialogue
            quac_data.append(dialogue_json)
        return quac_data
