import os
import sys

def get_path(*paths):
    '''
    获取程序运行根目录，传参可拼接。
    '''

    me = os.path.realpath(sys.argv[0])
    folder = os.path.dirname(me)
    return os.path.join(folder, *paths)

def get_configuration():
    '''
    '''

    