# coding=utf8

from utils.file_utils import FileUtil

file_util = FileUtil()
raw_data_file = '../data/cn_2_jp.txt'
process_data_file = '../data/cn_2_jp_process.txt'
encoding = 'utf-8'


def data_norm():
    raw_data = file_util.read_txt_file(raw_data_file, encoding)
    ret = []

    for line in raw_data:
        if line.startswith(u'【'):
            ret.append(line)
        else:
            ret[-1] += line

    return ret


def data_preprocess():
    data = data_norm()
    file_util.write_txt_file(process_data_file, data, encoding)


def main():
    data_preprocess()


if __name__ == '__main__':
    main()
