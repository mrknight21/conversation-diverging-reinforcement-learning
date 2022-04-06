from torch.utils.data import DataLoader
import json
import os
from tqdm import tqdm

def train(args):
    # load data
    print("[Loading data with batch size {}...]".format(args.batch_size))

    ROOT_DIR = "/home/mche618/conversation-diverging-reinforcement-learning/"

    with open(os.path.join(ROOT_DIR, args.data_dir, args.data_set_name + "_train.json")) as train_data:
        train_dataset = json.load(train_data)

    with open("../" + args.data_dir+args.data_set_name + "_valid.json") as valid_data:
        valid_dataset =json.load(valid_data)

    with open("../" + args.data_dir+args.data_set_name + "_test.json") as test_data:
        test_dataset = json.load(test_data)

    train_dataloader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
    valid_dataloader = DataLoader(valid_dataset, batch_size=args.batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=True)

    agent = setup_agent(args)


def setup_agent(args):
    a





