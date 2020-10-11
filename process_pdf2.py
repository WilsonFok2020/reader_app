# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:39:50 2020

@author: user
"""

import pdftotext
import os, pickle

input_dir = r'C:/Users/user/Documents/GitHub/My_other_repositories/reader_app/memo'

files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]

print ('len(files) ', len(files))

for file in files:
    # filename = 'the-anatomy-of-a-rally'
    filename = file.rstrip('.pdf')
    print (filename)
    with open(os.path.join(input_dir, filename + '.pdf'), "rb") as f:
        pdf = pdftotext.PDF(f)
    print ('len(pdf) ', len(pdf))
    
    pages = {i:page for i, page in enumerate(pdf)}
    pickle.dump(pages, open(os.path.join(input_dir, filename + '.p'), 'wb'))
    
    print ('---------------')

