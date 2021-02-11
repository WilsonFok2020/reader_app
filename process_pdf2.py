# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:39:50 2020

@author: user
"""

import pdftotext
import os, pickle

input_dir = r'C:/Users/user/Documents/GitHub/My_other_repositories/reader_app/memo'

files = [(folder, file) for folder in os.listdir(input_dir) for file in os.listdir(os.path.join(input_dir, folder)) if file.endswith('.pdf')]

print ('len(files) ', len(files))

for folder, file in files:
    # filename = 'the-anatomy-of-a-rally'
    '''
    
    strip all repeated chars
    
    i = 'ed.pdf'

    i.rstrip('.pdf')
    Out[28]: 'e'
    
    i = 'eddddd.pdf'
    
    i.rstrip('.pdf')
    Out[30]: 'e'

    '''
    filename = file.split('.')[0]
    print (filename)
    with open(os.path.join(input_dir, folder, filename + '.pdf'), "rb") as f:
        pdf = pdftotext.PDF(f)
    print ('len(pdf) ', len(pdf))
    
    pages = {i:page for i, page in enumerate(pdf)}
    pickle.dump(pages, open(os.path.join(input_dir, folder, filename + '.p'), 'wb'))
    
    print ('---------------')

