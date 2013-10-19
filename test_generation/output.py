import input
import unittest
import re
import itertools
    
#kiem tra 1 string co phai so hay khong
def check_int(s):
    if len(s) == 0:
        return False
    elif (s[0] == '-'):
        return s[1:].isdigit()
    else:
        return s.isdigit()


#kiem tra mien dau vao co hop le hay khong
def validinput(arr):
    check = 0
    for i in range(len(arr)):
        n = len(arr[i])/2
        for j in range(n):
            for k in range(j+1, n):
                if (arr[i][2*j] <= arr[i][2*k] and arr[i][2*j+1] >= arr[i][2*k]) or (arr[i][2*j] >= arr[i][2*k] and arr[i][2*j+1] <= arr[i][2*k]):
                   check +=1
    if(check == 0):
        return True
    else:
        return False


                   
#doc cac gia tri dau vao, neu hop le thi tach thanh cac lop tuong duong
#va tra ve gia tri dai dien cho moi lop, la gia tri giua.
#Hoac return false neu khong hop le
def read():
    doc = input.main.__doc__

    variables = (doc.split( ))
    num = len(variables) #so cac bien'
    boundary = [] #mang luu cac bien' va cac bien cua no
    
    for i in range(num):
        strv = re.split('[:;\]\[]', variables[i])
        k = 0
        boundary.append([])
        for j in range(len(strv)):
            if(check_int(strv[j])):
                boundary[i].append(int(strv[j]))
                k += 1
    if(validinput(boundary)):
        tb = [] #luu gia tri dai dien cho tung khoang cua bien
        for i in range(num):
            tb.append([])
            n = len(boundary[i])/2
            for j in range(n):
                gt = (boundary[i][2*j] + boundary[i][2*j+1])/2
                tb[i].append(gt)
        return tb
    else:
        return False

class TestSequense(unittest.TestCase):
    pass

def test_generator(*a):
    def test(self):
        self.assertEqual(input.main(*a), "aaa")
    return test
            

if __name__ == '__main__':
    if (read() != False):
        # luu cac gia tri test case
        tb = read()
        arr = []
        i = 0
        for element in itertools.product(*tb):
            arr[len(arr):]=[element]
            i+=1
            
        #tao va tu dong run test    
        j = 0
        for t in arr:
            test_name = 'test_%s' % str(j)
            test = test_generator(*t)
            setattr(TestSequense, test_name, test)
            j+=1
        unittest.main()
    else:
        raise Exception ('wrong input')
         



