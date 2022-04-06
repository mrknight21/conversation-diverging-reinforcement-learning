import argparse
from scripts.batch_supervised_training import train
import torch

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='datasets/data/', help='Directory for all data.')
    parser.add_argument('--data_set_name', type=str, default='dailydialogue', help='Name of the dataset.')
    parser.add_argument('--model_file', type=str, default='model.pt', help='Model file name.')
    parser.add_argument('--mode', default='train', choices=['train', 'predict', 'train_teacher', 'finetune'])
    parser.add_argument('--num_epoch', type=int, default=100)
    parser.add_argument('--batch_size', type=int, default=10)
    parser.add_argument('--log_step', type=int, default=20, help='Print log every k steps.')
    parser.add_argument('--model_dir', type=str, default='trained_model', help='Root dir for saving models.')

    parser.add_argument('--seed', type=int, default=1234)
    parser.add_argument('--cuda', type=bool, default=torch.cuda.is_available())
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--debug', action='store_true', help='Debug with dev set files')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.cuda:
        args.gpu = -1
    else:
        torch.cuda.set_device(args.gpu)
    print("Running with gpu: {}".format(args.gpu))
    train(args)


if __name__ == '__main__':
    main()
