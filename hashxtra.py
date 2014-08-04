#!/usr/bin/env python

import zlib


class crc32(object):
    name = 'crc32'
    digest_size = 4
    block_size = 1

    def __init__(self, arg=''):
        self.__digest = 0
        self.update(arg)

    def copy(self):
        copy = super(self.__class__, self).__new__(__class__)
        copy.__digest = self.__digest
        return copy

    def digest(self):
        return self.__digest

    def hexdigest(self):
        return '{:08x}'.format(self.__digest)

    def update(self, arg):
        self.__digest = zlib.crc32(arg, self.__digest) & 0xffffffff

#class tiger192(object):
#    name = 'tiger192'
#    digest_size = 192
#    block_size = 1
#
#    def __init__(self, arg=''):
#        self.__digest = 0
#        self.update(arg)
#
#    def copy(self):
#        copy = super(self.__class__, self).__new__(__class__)
#        copy.__digest = self.__digest
#        return copy
#
#    def digest(self):
#        return self.__digest
#
#    def hexdigest(self):
#        return '{:08x}'.format(self.__digest)
#
#    def update(self, arg):
#        self.__digest = tiger.(arg, self.__digest) & 0xffffffff
