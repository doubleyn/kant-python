# shopping cart 클래스 선언
class ShoppingCart:
    def __init__(self):
        self.items = []

    # 상품 목록 저장 기능
    # 메서드
    # - 장바구니 담기
    def add(self, item):
        self.items.append(item)
    # - 장바구니 빼기
    def remove(self, item):
        self.items.remove(item)

    # 상품 목록 조회
    def show_items(self):
        return self.items

# 상품 클래스
class Product:
    def __init__(self, name, price):
# 속성
# - 제품명
        self.name = name
# - 가격
        self.price = price

    def __repr__(self):
        return f"제품명: {self.name}, 가격: {self.price}원"

# 상품 3개 생성
product_a = Product("이클립스", 3000)
product_b = Product("새콤달콤", 1000)
product_c = Product("밴드", 2000)

# 쇼핑 카트 생성
shopping_cart_a = ShoppingCart()

# 상품 1개 장바구니 담기
shopping_cart_a.add(product_a)
# 상품 1개 장바구니 담기
shopping_cart_a.add(product_b)
# 상품 1개 장바구니 담기
shopping_cart_a.add(product_c)
# 상품 1개 장바구니에서 빼기
shopping_cart_a.remove(product_b)
# 장바구니에 담긴 상품 목록 조회
# print(shopping_cart_a.show_items())
for item in shopping_cart_a.show_items():
    print(item)