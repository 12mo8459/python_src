# class People():
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.addr = None

# h1 = People()
# print(h1.addr)
# h2 = People()
# print(h1.addr)

class Product():
    serial_num = 0

    def __init__(self):
        Product.serial_num += 1
        self.serial_num = Product.serial_num
        self.name = None

#if __name__ == 'main':
tv1 = Product()
tv2 = Product()
tv3 = Product()
print(tv1.serial_num, tv2.serial_num, tv3.serial_num)