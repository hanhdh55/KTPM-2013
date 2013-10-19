# Do Thanh Trung - 10020382
# output.py

import input
import itertools
import unittest

arr = [] # mang chua cac gia tri dai dien
arr2 = [] # mang chua cac khoang gia tri
docstring = input.main.__doc__

# dua cac dau vao vao mang

i = 0
j = -1
k = 0
try:
    while(i<len(docstring)):
        if((i+1)<len(docstring) and docstring[i+1]==':'): 
            j+=1
            arr.append([])
            arr2 = []
            k = 0
        tmp = ''
        if(docstring[i]=='['): 
            arr2.append([])
            i = i+1
            while(docstring[i]!=';'): # bien dau
                tmp += docstring[i]
                i+=1
            a = int(tmp)
            tmp = ''
            i+=1
            while(docstring[i]!=']'): # bien cuoi
                tmp += docstring[i]
                i+=1
            b = int(tmp)
            arr[j].append((a+b)/2) #them gia tri dai dien cho moi khoang
            tmp = ''
            
            #xet lop tuong duong
            arr2[k].append(a)
            arr2[k].append(b)
            q = 0
            while(q < k):
                if(arr2[q][0]<=a<=arr2[q][1] or arr2[q][0]<=a<=arr2[q][1]
                   or a<=arr2[q][0]<=b or a<=arr2[q][1]<=b):
                    raise Exception("wrong input")
                q+=1
            k+=1 
        i+=1
    
    class output(unittest.TestCase):
        pass
    def test_generator(*args):
        def test(self):
            self.assertEqual(input.main(*args),1)
        return test
    if __name__ == '__main__':
        for element in itertools.product(*arr):
            test_name = 'test_' + str(element)
            test = test_generator(*element)
            setattr(output, test_name, test)
        unittest.main()
except Exception as e:
    raise
