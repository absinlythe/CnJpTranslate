# coding=utf8

import os


class FileUtil:
    def __init__(self):
        pass

    def read_txt_file(self, file_name, decode):
        if not file_name or not decode:
            return

        if not os.path.exists(file_name):
            print "file %s not exists" % file_name

        f = open(file_name, 'r')
        data = [line.strip().decode(encoding=decode) for line in f.readlines()]
        f.close()

        return data

    def write_txt_file(self, file_name, data, encode):
        if not file_name or not data or not encode:
            return

        f = open(file_name, 'w')

        for line in data:
            f.write(line.encode(encoding=encode) + '\r')

        f.close()
