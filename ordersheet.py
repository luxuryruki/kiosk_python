class Ordersheet:
    def __init__(self, order_id):
        self.order_id = order_id
        self.total_price = 0
        self.items = []


    def add_item(self, product_name, price, quantity=1):
        """주문 항목 추가"""
        for item in self.items:
            if item['product_name'] == product_name:
                item['quantity'] += quantity
                self.update_total_price()
                return
        self.items.append({'product_name': product_name, 'price': price, 'quantity': quantity})
        self.update_total_price()

    def remove_item(self, product_name):
        """주문 항목 삭제"""
        self.items = [item for item in self.items if item['product_name'] != product_name]
        self.update_total_price()

    def update_quantity(self, product_name, change):
        """주문 항목 수량 변경"""
        for item in self.items:
            if item['product_name'] == product_name:
                item['quantity'] += change
                if item['quantity'] <= 0:  # 수량이 0 이하일 경우 항목 삭제
                    self.remove_item(product_name)
                self.update_total_price()
                return

    def update_total_price(self):
        """총 가격 계산"""
        self.total_price = sum(item['price'] * item['quantity'] for item in self.items)

    def total_items(self):
        """총 항목 수 계산"""
        return sum(item['quantity'] for item in self.items)
    
    def get_id(self):
        return self.order_id
    def get_items(self):
        return self.items