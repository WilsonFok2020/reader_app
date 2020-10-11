# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 08:39:57 2020

@author: user
"""
# m00nlight github
class KMP:
    def partial(self, pattern):
        
        ret = [0]
        for i in range(1, len(pattern)):
            j = ret[i-1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j-1]
            ret.append(j+1 if pattern[j] == pattern[i] else j)
            
        return ret
    
    def search(self, T,P):
        
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j-1]
            if T[i] == P[j]:
                j += 1
            if j == len(P):
                ret.append(i-(j-1))
                j = partial[j-1]
                
        return ret
    
def test():
    
    p1 = 'aa'
    t1 = 'aaaaaaaa'
    
    kmp = KMP()
    assert(kmp.search(t1, p1) == [0,1,2,3,4,5,6])
    
    p2 = 'abc'
    t2 = 'avdabeabfabc'
    
    assert(kmp.search(t2, p2) == [9])
    
    p3 = 'aab'
    t3 = 'aaabaacbaab'
    
    assert(kmp.search(t3,p3) == [1,8])
    
    
    p4 = 'ionioj'
    t4 = 'abcionioniojondfeg'
    assert(kmp.search(t4, p4) == [6])
    
    p5 = 'pok'
    t5  = 'werwerwerwer234234po'
    assert(kmp.search(t5, p5) == [])
    
    print ('pass')

if __name__ == "__main__":
    test()