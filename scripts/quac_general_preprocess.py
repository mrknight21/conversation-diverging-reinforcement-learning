from preprocessors.quac_general_processor import QuacGeneralProcessor
import argparse
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG,
                    datefmt='%m/%d/%Y %I:%M:%S')
log = logging.getLogger(__name__)

def main(args):
    preprocessor = QuacGeneralProcessor(args)
    preprocessor.run()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Preprocessing train + dev files, about 20 minutes to run on Servers.'
    )
    parser.add_argument('--train_file', default='/home/mche618/ParlAI/data/QuACFull/train_v0.2.json',
                        help='path to quac train file.')
    parser.add_argument('--dev_file', default='/home/mche618/ParlAI/data/QuACFull/val_v0.2.json',
                        help='path to quac dev file.')
    parser.add_argument('--save_train_file', default='/home/mche618/data/quac_interview/pro_train.msgpack',
                        help='save path to quac train file.')
    parser.add_argument('--save_dev_file', default='/home/mche618/data/quac_interview/pro_dev.msgpack',
                        help='save path to quac dev file.')
    args = parser.parse_args()
    log.info('start general data preparing... ')
    main(args)
