class Product:
    counte = 0
    def __init__(self, product_name, product_price, product_stock):
        # product.count += 1
        self.product_name = product_name
        self._product_price = product_price
        self._product_stock = product_stock

    def product_price(self):
        return self._product_price
    def product_price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._product_price = value

    def product_stock(self):
        return self._product_stock
    def product_stock(self, value):
        if value < 0:
            print("Stock cannot be negative.")
        else:
            self._product_stock = value

products = [
    Product("Laptop", 1500, 10),
    Product("Smartphone", 800, 20),
    Product("Tablet", 600, 15)

]

#노북 가격 20% 할인
products[0].product_price(products[0].product_price() * 0.8) # 20% discount
#스트폰 가격 10% 인상
products[1].product_price(products[1].product_price() * 1.1) # 10% increase
#전제품출력
for p in products:
    print(f"Product: {p.product_name}, Price: {p.product_price()}, Stock: {p.product_stock()}")
