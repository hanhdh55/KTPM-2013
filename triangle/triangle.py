import math

def detect_triangle(a, b, c):
   
    e = 10**-9
    if  ((type(a) in [float, int, long]) and (type(b) in [float, int, long]) and (type(c) in [float, int, long])):
        if  (a>0 and b>0 and c>0 and a <= 2**32 - 1 and b<=2**32 - 1 and c<=2**32 - 1):
            if a+b>c and b+c>a and a+c>b:
                if a==b and b==c:
                    return "ba canh la tam giac deu"
                elif (b==c and math.fabs(a*a - b*b - c*c) < e) or (a==c and math.fabs(b*b - c*c - a*a )< e) or (a==b and math.fabs(c*c - a*a - b*b )< e):
                    return "ba canh la tam giac vuong can"
                elif (a==b or b==c or c==a):
                    return "ba canh la tam giac can"
                elif ( math.fabs(a*a - b*b - c*c) < e) or (math.fabs(b*b - c*c - a*a )< e) or (math.fabs(c*c - a*a - b*b )< e):
                    return "ba canh la tam giac vuong"
                else: 
                    return "ba canh la tam giac thuong"
            else:
                return "khong phai tam giac"
        else:
            return "khong nam trong mien gia tri"
    else:
        return "du lieu khong hop le"


