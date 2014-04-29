#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 - cenyongh <cenyongh@gmail.com>
#

import os

def cleanup(file_path):
    file = open(file_path,'rb')
    
    content = file.read() 
    i = content.find('APETAGEX')
    if i != -1:
        print 'cleanup %s' % file_path
        file = open(file_path,'wb')
        file.write(content[:i])
        file.close()

if __name__ == '__main__':
    BASE_DIR = '/storage/Media/Audio/Music'
    for dirpath, dirnames, filenames in os.walk(BASE_DIR):
        for filename in filenames:
            cleanup(os.path.join(dirpath,filename))
