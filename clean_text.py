# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:09:10 2020

@author: user
"""

import os, pickle
from string_search import KMP
from collections import namedtuple
import re


def crop(match, s, kmp):
    
    # assert len(match) >= 2
    start, end = match[0], match[-1]
    start_ind = kmp.search(s, start)
    end_ind = kmp.search(s, end)
    
    start_ind = start_ind[0]
    end_ind = end_ind[-1] + len(end)
    
    # print (s[start_ind:end_ind])
    return s[start_ind:end_ind]


def sieve_line(lines, kmp, name):
    
    characters = [non_whitespace.findall(line) for line in lines]  
    
    # at least 2 characters or more
    # note: daggling.. word fails
    filtered = [crop(match, line, kmp) for match, line in zip(characters, lines) if len(match) >= 1 ]
    
    
    with open(name+'.txt', 'w') as f:
        for line in filtered:
            f.write(line)
            f.write('\n')
            
    
    return filtered

def check_underline(s):
    
    index = [ i for i, c in enumerate(s) if c == 'U']
    
    if len(index) < 2:
        return False
    
    inbetween = s[index[0]+1:index[-1]-1]
    ans = non_whitespace.findall(inbetween)
    
    if len(ans) == 0:
        return True
    else:
        return False
    
    
def remove_speical_char(special_char, lines):
    new = []
    for line in lines:
        dropped = [c for c in line if c not in special_char]
        new.append(''.join(dropped))
        
    return new

def check_int(x):
    
    try: 
        int(x)
    except ValueError as e:
        return False
    else:
        return True


def stitching(dry_lines):
    
    # stitch if first char is lower
    stitched = []
    current_line = dry_lines[0]
    s = []
    
    for i in range(1, len(dry_lines)):
        look_at = dry_lines[i]
        c = look_at[0]
        
        if c.islower()  or check_int(c):
            s.append(i)
            
        elif c.isupper():
            L = len(s)
            if L == 0:
                
                stitched.append(current_line)
                current_line = look_at
                
            elif L > 0:
                concatenated = current_line
                for si in s:
                    concatenated += ' ' + dry_lines[si]
                stitched.append(concatenated)
                s = []
                
                current_line = look_at
                
    # handle the last step
    L = len(s)
    if L == 0:
        
        stitched.append(current_line)        
    elif L > 0:
        concatenated = current_line
        for si in s:
            concatenated += ' ' + dry_lines[si]
        stitched.append(concatenated)
        
    return stitched
  
def merge_short_sentences(stitched):
    
    # one word sentence    
    num_words = [len(line.split(' ')) for line in stitched]
    merged = [i for i, n in enumerate(num_words) if n < 7]
    
    if len(stitched) -1 in merged:
        merged.pop(merged.index(len(stitched)-1)) # ignore the last sentence
        
    for merged_index in merged:
        stitched[merged_index] = stitched[merged_index] + ' ' + stitched[merged_index+1]
        
    # update to show 
    merged = [i+1 for i in merged]
        
    merged_lines = [line for i, line in enumerate(stitched) if i not in merged]
    return merged_lines

    
def process(lines, lines2):
    
    
    
    lines = remove_speical_char(special_char, lines)
    lines2 = remove_speical_char(special_char, lines2)
    
    lines = [line.replace('-', ' ') for line in lines]
    lines2 = [line.replace('-', ' ') for line in lines2]
    
    # remove blank lines why, 1) no information, 2) no needed in audio 3) save time
    lines = sieve_line(lines, kmp, name='lines') 
    lines2 = sieve_line(lines2, kmp, name='lines2')
    
    
    
    new = []
    for line in lines:
        # +1 needed so that the fullstop stays with the sentence
        # dot_ind = [i+1 for i, c in enumerate(line) if c == '.']
        dot_ind = [i for i, c in enumerate(line) if c == '.']
        
        # check for abbreviations
        # char before is upper,  and the char after is a whitespace
        
        no_abbre = []
        for i in dot_ind:
            
            try:
                status = line[i-1].isupper() or check_int(line[i-1])
            except IndexError as e:
                print (e, line)
                status = False
                
            try:
                status2 = line[i+1].isupper() or check_int(line[i+1])
            except IndexError as e:
                print (e, line)
                status2 = False
                
            try:
                status3 = line[i+3].islower()
            except IndexError as e:
                print (e, line)
                status3 = False
                
            if status and (status2 or status3):
                print ('abbreviation : ', line)
                print (i)
            else:
                no_abbre.append(i)
                
        
        
        if len(no_abbre) == 0:
            new.append(line)
        else:
            
            sublines = []
            no_abbre = [i+1 for i in no_abbre]
            no_abbre = [0] + no_abbre + [len(line)]
            
            print (line, no_abbre)
            for start, end in zip(no_abbre[0:-1], no_abbre[1:]):
                sublines.append(line[start:end])
                
            new += sublines
            
    new = sieve_line(new, kmp, name='break_by_fullstop')
            


    watermark = []
    dry_lines = []    
    
    for i, pattern in enumerate(new):
        
        for j, line in enumerate(lines2):
            
            ans = kmp.search(line, pattern)
            
            if len(ans) > 0:
                watermark.append(Row(i,j,ans))
                break
            
        else:
            
            if not check_underline(pattern):
                dry_lines.append(pattern)
            
                
            



    with open('watermark.txt', 'w') as f:
        
        previous_pattern = None
        for row in watermark:
            
            if previous_pattern != row.pattern:
                # print ('pattern ', lines[row.pattern])
                f.write('pattern {} : {} \n'.format(row.pattern, new[row.pattern]))
                
                previous_pattern = row.pattern
                
            # print ('template ', lines2[row.template])
            f.write('template {} : {} \n'.format(row.template, lines2[row.template]))
            
    
    phrase_dir = r'C:\Users\user\Documents\Nvidia\PyTorch\SpeechSynthesis\Tacotron2\phrases'
    with open(os.path.join(phrase_dir, 'dry_lines.txt'), 'w', encoding='utf-8') as f:
        for line in dry_lines:
            f.write(line)
            f.write('\n')
            
            
    # almost right rule
    stitched = stitching(dry_lines)
    merged_lines = merge_short_sentences(stitched)
    
                
    with open(os.path.join(phrase_dir, 'concatenated_lines.txt'), 'w', encoding='utf-8') as f:
        for line in merged_lines:
            f.write(line)
            f.write('\n')
    


if __name__ == "__main__":
    # check for non-white space
    non_whitespace = re.compile(r'\S+')
    special_char = ['•', '“', '”','©', '(', ')']
    input_dir = r'C:/Users/user/Documents/GitHub/My_other_repositories/reader_app/'
    kmp = KMP()
    Row = namedtuple('Row', ['pattern', 'template', 'location'])
    

    
    
    
    
    # filename = 'the-anatomy-of-a-rally'
    filename = '1990-10-12-the-route-to-performance'
    pages = pickle.load(open(os.path.join(input_dir, filename + '.p'), 'rb'))


    lines = pages[1].split('\n')    
    lines2 = pages[0].split('\n')
    
    process(lines, lines2)
    
    
    
                
            
    
        





    

        

        
        
























