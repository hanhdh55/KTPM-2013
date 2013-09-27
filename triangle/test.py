import unittest
import math
import triangle

class testTriangle(unittest.TestCase):

    def test_kieuDulieuBienA_true(self):
        self.assertEqual(triangle.detect_triangle('a', 4, 4), "du lieu khong hop le")
        
    def test_kieuDulieuBienB_true(self):
        self.assertEqual(triangle.detect_triangle(4,'b', 4), "du lieu khong hop le")

    def test_kieuDulieuBienC_true(self):
        self.assertEqual(triangle.detect_triangle(4, 4, 'c'), "du lieu khong hop le")
        
       
    def test_MienGiaTriTrenA(self):
        self.assertEqual(triangle.detect_triangle((2**32 - 1) + 1, 2, 3), "khong nam trong mien gia tri")

    def test_MienGiaTriTrenB(self):
        self.assertEqual(triangle.detect_triangle(10, (2**32 - 1) + 1,3), "khong nam trong mien gia tri")

    def test_MienGiaTriTrenC(self):
        self.assertEqual(triangle.detect_triangle(12, 24, (2**32 - 1) + 1), "khong nam trong mien gia tri")


    def test_MienGiaTriDuoiA(self):
        self.assertEqual(triangle.detect_triangle(0, 2, 3), "khong nam trong mien gia tri")

    def test_MienGiaTriDuoiB(self):
        self.assertEqual(triangle.detect_triangle(10, 0, 3), "khong nam trong mien gia tri")

    def test_MienGiaTriDuoiC(self):
        self.assertEqual(triangle.detect_triangle(12, 24, 0), "khong nam trong mien gia tri")

    def test_TamgiacDeu(self):
        self.assertEqual(triangle.detect_triangle(100.0, 100.0, 100.0), "ba canh la tam giac deu")


    def test_TamgiacVuongcanTaiA(self):
        self.assertEqual(triangle.detect_triangle(math.sqrt(2), 1, 1), "ba canh la tam giac vuong can")

    def test_TamgiacVuongcanTaiB(self):
        self.assertEqual(triangle.detect_triangle(10.0, math.sqrt(200.0), 10.0), "ba canh la tam giac vuong can")
        
    def test_TamgiacVuongcanTaiC(self):
        self.assertEqual(triangle.detect_triangle(10, 10, math.sqrt(200)), "ba canh la tam giac vuong can")

        
    def test_TamgiacCan1A(self):
        self.assertEqual(triangle.detect_triangle(10, 2**32 - 1, 2**32 - 1), "ba canh la tam giac can")

    def test_TamgiacCan1B(self):
        self.assertEqual(triangle.detect_triangle(2**32 - 1,10000.0, 2**32 - 1), "ba canh la tam giac can")

    def test_TamgiacCan1C(self):
        self.assertEqual(triangle.detect_triangle(2**32 - 1, 2**32 - 1, 6), "ba canh la tam giac can")


    def test_TamgiacCan2A(self):
        self.assertEqual(triangle.detect_triangle(10, 7, 7), "ba canh la tam giac can")

    def test_TamgiacCan2B(self):
        self.assertEqual(triangle.detect_triangle(8099.10,10000.0, 8099.10), "ba canh la tam giac can")
 
    def test_TamgiacCan2C(self):
        self.assertEqual(triangle.detect_triangle(0.11111, 0.11111, 0.2), "ba canh la tam giac can")


    def test_TamgiacVuongA(self):
        self.assertEqual(triangle.detect_triangle(3, 4, 5), "ba canh la tam giac vuong")

    def test_TamgiacVuongB(self):
        self.assertEqual(triangle.detect_triangle(100.0, 120.0, math.sqrt(24400)), "ba canh la tam giac vuong")

    def test_TamgiacVuongC(self):
        self.assertEqual(triangle.detect_triangle(3, 4, 5), "ba canh la tam giac vuong")

    def test_TamgiacThuong1(self):
        self.assertEqual(triangle.detect_triangle(1123, 3433, 4232),"ba canh la tam giac thuong")

    def test_TamgiacThuong2(self):
        self.assertEqual(triangle.detect_triangle(2**32 - 100, 2**32 - 500, 500),"ba canh la tam giac thuong")


    def test_KhongphaiTamgiac(self):
        self.assertEqual(triangle.detect_triangle(2, 2, 4), "khong phai tam giac")

if __name__ == '__main__':
    unittest.main()
