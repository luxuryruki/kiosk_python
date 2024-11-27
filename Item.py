class Item:
    def __init__(self, product_name, price, quantity=1):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, change):
        """상품 수량 변경"""
        self.quantity += change

    def total_price(self):
        """상품 총 가격 계산"""
        return self.price * self.quantity