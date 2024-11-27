import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox  
from data_structures.queue import Queue
from ordersheet import Ordersheet

# 예시 데이터
ready_list = []  # 준비완료 리스트
pending_list = Queue()  # 준비중 리스트
cart = {} 
order_number = 100

# 메인 윈도우 생성
root = tk.Tk()
root.title("상품 주문 화면")
root.geometry("1400x800")  # 창 크기 설정

# 두번째 윈도우 생성
second_window = tk.Toplevel(root)
second_window.title("상품 처리 화면")
second_window.geometry("700x800")

# 왼쪽: 주문 목록 표시 영역
left_frame = tk.Frame(second_window, bg="white", relief="solid", borderwidth=1, width=200)
left_frame.pack(side="left", fill="y")
left_frame.pack_propagate(False)  # 프레임 크기 고정

# 왼쪽 주문 목록 제목
tk.Label(left_frame, text="주문 목록", font=("Arial", 20), bg="white").pack(pady=10)

# 오른쪽: 주문 상세 표시 영역
right_frame = tk.Frame(second_window, bg="white", relief="solid", borderwidth=1, width=400)
right_frame.pack(side="right", fill="both", expand=True)

# 상단: 주문 번호 표시 영역
top_frame = tk.Frame(right_frame, bg="white", relief="solid", borderwidth=1, height=100)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

# 중단: 주문 내역 표시 영역
middle_frame = tk.Frame(right_frame, bg="white", relief="solid", borderwidth=1)
middle_frame.pack(fill="both", expand=True)
middle_frame.pack_propagate(False)

# 하단: 주문 처리 버튼 영역
bottom_frame = tk.Frame(right_frame, bg="white", relief="solid", borderwidth=1, height=60)
bottom_frame.pack(fill="x")
bottom_frame.pack_propagate(False)

# 예제: 각 프레임에 Label 추가 (필요에 따라 내용 업데이트)
tk.Label(top_frame, text="주문 번호", font=("Arial", 36), bg="white").pack(expand=True)
tk.Label(middle_frame, text="주문 내역", font=("Arial", 24), bg="white").pack(pady=10)



# 주문 처리 버튼
tk.Button(
    bottom_frame, 
    text="주문 처리", 
    font=("Arial", 20), 
    bg="#4CAF50", 
    fg="black", 
    command=lambda: process_order()
).pack(pady=10, padx=20, expand=True)

def process_order():
    """주문 처리 로직 (추후 구현 예정)"""
    pass  # 현재는 구현 없음


products = {
    "도너츠": [("초코 도너츠", 1000, "images/donut1.png"), ("슈가 도너츠", 1000, "images/donut1.png"), ("크림 도너츠", 1000, "images/donut1.png"), ("초코 도너츠", 1000, "images/donut1.png"), ("슈가 도너츠", 1000, "images/donut1.png"), ("크림 도너츠", 1000, "images/donut1.png")],
    "찐빵": [("팥 찐빵", 1000, "images/donut1.png"), ("야채 찐빵", 1000, "images/donut1.png"), ("고구마 찐빵", 1000, "images/donut1.png")],
    "음료": [("아메리카노", 1000, "images/donut1.png"), ("라떼", 1000, "images/donut1.png"), ("녹차", 1000, "images/donut1.png")]
}


# 왼쪽 준비 영역 (상단: 준비완료, 하단: 준비중)
left_frame = tk.Frame(root, width=300, height=800, bg="white", relief="solid", borderwidth=1)
left_frame.pack(side="left", fill="y")
left_frame.pack_propagate(False)  # 프레임 내부 내용에 따라 크기 변경 안 되도록 설정

# 상단 준비완료 영역
upper_frame = tk.Frame(left_frame, bg="white", relief="solid", borderwidth=1, height=400)
upper_frame.pack(fill="x", side="top")  # 위쪽에 배치
upper_frame.pack_propagate(False)
tk.Label(upper_frame, text="준비완료", font=("Arial", 24), width=20, height=2, bg="white").pack(pady=10)

# 준비완료 리스트 번호 표시
def update_ready_display():
    """준비완료 영역 업데이트"""
    for widget in upper_frame.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") != "준비완료":
            widget.destroy()  # 기존 준비완료 리스트 제거

    ready_numbers = ", ".join(map(str, ready_list))  # 리스트를 문자열로 변환
    tk.Label(upper_frame, text=ready_numbers, font=("Arial", 20), anchor="w", bg="white").pack(pady=10, padx=10, fill="x")

# 하단 준비중 영역
lower_frame = tk.Frame(left_frame, bg="white", relief="solid", borderwidth=1, height=400)
lower_frame.pack(fill="x", side="top")  # 아래쪽에 배치
lower_frame.pack_propagate(False)
tk.Label(lower_frame, text="준비중", font=("Arial", 24), width=20, height=2, bg="white").pack(pady=10)


# 중앙 카테고리와 상품 표시 영역
center_frame = tk.Frame(root, width=600, height=800, bg="white", relief="solid", borderwidth=1)
center_frame.pack(side="left", fill="both", expand=True)

category_frame = tk.Frame(center_frame, height=50, bg="white", relief="solid", borderwidth=1)
category_frame.pack(side="top", fill="x")

# 버튼 중앙 정렬
category_frame.columnconfigure(0, weight=1)
category_frame.columnconfigure(1, weight=1)
category_frame.columnconfigure(2, weight=1)

# 카테고리 버튼
category_frame.columnconfigure(0, weight=1)  # 첫 번째 버튼
category_frame.columnconfigure(1, weight=1)  # 두 번째 버튼
category_frame.columnconfigure(2, weight=1)  # 세 번째 버튼

# 도너츠 버튼
tk.Button(
    category_frame,
    text="도너츠",
    font=("Arial", 24, "bold"),  # 글꼴과 크기 강조
    width=15,  # 버튼 너비
    height=2,  # 버튼 높이
    bg="#FFE4B5",  # 밝은 베이지 색상 배경
    activebackground="#FFDAB9",  # 활성화 배경 색
    relief="flat",  # 테두리 스타일
    command=lambda: display_products("도너츠")
).grid(row=0, column=0, padx=10, pady=10)

# 찐빵 버튼
tk.Button(
    category_frame,
    text="찐빵",
    font=("Arial", 24, "bold"),
    width=15,
    height=2,
    bg="#FFFACD",  # 밝은 노란색 배경
    activebackground="#FAFAD2",
    relief="flat",
    command=lambda: display_products("찐빵")
).grid(row=0, column=1, padx=10, pady=10)

# 음료 버튼
tk.Button(
    category_frame,
    text="음료",
    font=("Arial", 24, "bold"),
    width=15,
    height=2,
    bg="#E0FFFF",  # 밝은 파란색 배경
    activebackground="#AFEEEE",
    relief="flat",
    command=lambda: display_products("음료")
).grid(row=0, column=2, padx=10, pady=10)


product_display = tk.Frame(center_frame, bg="white")
product_display.pack(fill="both", expand=True)


# 오른쪽 주문 내역 및 결제 영역 (절대 크기 설정)
right_frame = tk.Frame(root, width=300, height=800, bg="white", relief="solid", borderwidth=1)
right_frame.pack(side="right", fill="y")
right_frame.pack_propagate(False)

# 주문 내역 리스트 영역
order_list = tk.Frame(right_frame, bg="white")
order_list.pack(fill="both", expand=True)

# 합계 및 결제 버튼 영역
total_frame = tk.Frame(right_frame, bg="white", relief="flat")  # flat로 기본 테두리 제거
total_frame.pack(side="bottom", fill="x", pady=10)





def display_products(category):
    """카테고리 버튼 클릭 시 상품 표시"""
    # 기존 상품 클리어
    for widget in product_display.winfo_children():
        widget.destroy()

    # 그리드 정렬을 위한 중앙 설정
    product_display.columnconfigure(0, weight=1)  # 왼쪽 여백
    product_display.columnconfigure(1, weight=1)  # 왼쪽 첫 번째 메뉴
    product_display.columnconfigure(2, weight=1)  # 두 번째 메뉴
    product_display.columnconfigure(3, weight=1)  # 세 번째 메뉴
    product_display.columnconfigure(4, weight=1)  # 오른쪽 여백

    if category in products:
        row = 0
        col = 1  # 첫 번째 메뉴는 두 번째 컬럼(인덱스 1)에 위치
        for product_name, price, img_path in products[category]:
            # 상품 프레임
            frame = tk.Frame(product_display, bg="white", padx=10, pady=10)
            frame.grid(row=row, column=col, sticky="n")

            # 이미지 로드
            try:
                photo = tk.PhotoImage(file=img_path)
                photo = photo.subsample(3, 3)  # 이미지 크기 조정 (축소)
            except Exception as e:
                photo = None  # 이미지 로드 실패 시 None 처리

            # 내부 중앙 정렬을 위한 서브 프레임
            inner_frame = tk.Frame(frame, bg="white")
            inner_frame.pack(expand=True)

            # 이미지
            if photo:
                img_label = tk.Label(inner_frame, image=photo, bg="white")
                img_label.image = photo  # 이미지 참조 유지
                img_label.pack(pady=5)

            # 가격 표시
            tk.Label(inner_frame, text=f"₩{price:,}", font=("Arial", 20), bg="white").pack(pady=5)

            # 상품 버튼
            tk.Button(
                inner_frame, 
                text=product_name, 
                font=("Arial", 20), 
                width=15, 
                height=1, 
                command=lambda p=product_name: add_to_cart(p)
            ).pack(pady=10)

            # 다음 위치 계산
            col += 1
            if col > 3:  # 세 번째 메뉴까지 채우면 다음 행으로 이동
                col = 1
                row += 1



def update_order_display():
    """주문 내역 UI 업데이트"""
    # 기존 주문 내역 삭제
    for widget in order_list.winfo_children():
        widget.destroy()

    # 장바구니가 비어 있을 때
    if not cart:
        spacer = tk.Frame(order_list, height=50, bg="white")  # 빈 공간 추가
        spacer.pack()  # 상단에 추가로 여백 확보

        tk.Label(order_list, text="장바구니가 비어 있습니다.", font=("Arial", 20), bg="white").pack(pady=10)
    
    # 장바구니에 있는 상품 표시
    total_price = 0
    total_quantity = 0
    for product_name, (quantity, price, item_total_price) in cart.items():
        frame = tk.Frame(order_list, bg="white")
        frame.pack(fill="x", pady=5)

        # 왼쪽: 상품명 표시
        tk.Label(frame, text=f"{product_name}", font=("Arial", 20), bg="white", anchor="w").pack(side="left", padx=5)

        # 오른쪽: 수량 조정 버튼 및 수량 표시
        controls_frame = tk.Frame(frame, bg="white")
        controls_frame.pack(side="right", padx=10)

        # + 버튼
        tk.Button(
            controls_frame, text="+", font=("Arial", 20), command=lambda p=product_name: (update_quantity(p, 1),print(cart))
            
        ).pack(side="left", padx=2)

        # 수량 표시    
        tk.Label(controls_frame, text=f"{quantity}", font=("Arial", 20), bg="white").pack(side="left", padx=5)
        
        # - 버튼
        tk.Button(
            controls_frame, text="-", font=("Arial", 20), command=lambda p=product_name: (update_quantity(p, -1),print(cart))
        ).pack(side="left", padx=2)

        # 가격 계산
        total_price += quantity * price
        total_quantity += quantity

    # 기존 총합 영역 삭제
    for widget in total_frame.winfo_children():
        widget.destroy()

    # 총 수량 및 총 가격 표시
    tk.Label(total_frame, text=f"{total_quantity}개", font=("Arial", 24), anchor="e", bg="white").pack(pady=5, fill="x")
    tk.Label(total_frame, text=f"{total_price:,}원", font=("Arial", 24), anchor="e", bg="white").pack(pady=5, fill="x")

    # 결제하기 버튼
    tk.Button(
        total_frame, 
        text="주문 하기", 
        font=("Arial", 24), 
        bg="white", 
        fg="black", 
        width=15, 
        height=2, 
        command=place_order
    ).pack(pady=10)

def update_quantity(product_name, change):
    """상품 수량 변경"""
    if product_name in cart:
        cart[product_name][0] += change
        if cart[product_name][0] <= 0:  # 수량이 0 이하인 경우 삭제
            del cart[product_name]
        else:
            cart[product_name][2] = cart[product_name][0] * cart[product_name][1]
    update_order_display()


def place_order():
    """주문 처리"""
    global order_number  # 주문 번호를 전역 변수로 사용
    new_ordersheet = create_ordersheet_from_cart(order_id=order_number, cart=cart)
    if cart:  # 장바구니에 상품이 있는 경우에만 처리
        # 주문 완료 메시지
        messagebox.showinfo(
            "주문 완료",
            f"주문이 완료되었습니다!\n주문번호: {order_number}"
        )

        # 주문 번호를 대기 목록에 추가
        pending_list.enqueue(new_ordersheet)
        # 주문 번호 증가
        order_number += 1

        # 장바구니 초기화 및 UI 업데이트
        cart.clear()
        update_order_display()
        update_pending_display()
    else:
        # 장바구니 비어 있을 때 경고 메시지
        messagebox.showwarning("장바구니 비어 있음", "장바구니가 비어 있습니다. 주문을 추가하세요.")


def create_ordersheet_from_cart(order_id, cart):
    """주문 번호와 카트를 기반으로 Ordersheet 생성"""
    new_order = Ordersheet(order_id)
    for product_name, (quantity, unit_price, total_price) in cart.items():
        new_order.add_item(product_name=product_name, price=unit_price, quantity=quantity)
    return new_order

def update_pending_display():
    """하단 준비 중 영역 UI 업데이트"""
    # 기존 위젯 삭제
    for widget in lower_frame.winfo_children():
        widget.destroy()

    # '준비중' 제목 표시
    tk.Label(lower_frame, text="준비중", font=("Arial", 24), width=20, height=2, bg="white").pack(pady=10)

    # 대기 중인 주문 번호 표시
    if not pending_list.is_empty():  # 큐가 비어 있지 않을 때
        # CList를 순회하여 order_id 추출
        current = pending_list.clist.head

        # current가 없거나 next가 없는 경우 처리하지 않음
        if not current or not current.next_node:
            tk.Label(lower_frame, text="대기 중인 주문이 없습니다.", font=("Arial", 20), bg="white").pack(pady=10)
            return

        # CList 순회
        order_ids = []
        for _ in range(pending_list.size):
            order_ids.append(current.value.get_id())  # Ordersheet의 get_id 메서드 호출
            current = current.next_node  # 다음 노드로 이동

        # 추출한 주문 번호를 화면에 표시
        pending_numbers = ", ".join(map(str, order_ids))
        tk.Label(lower_frame, text=pending_numbers, font=("Arial", 20), anchor="w", bg="white").pack(pady=10, padx=10, fill="x")
    else:
        # 대기 중인 주문이 없을 때 메시지 표시
        tk.Label(lower_frame, text="대기 중인 주문이 없습니다.", font=("Arial", 20), bg="white").pack(pady=10)


def add_to_cart(product_name):
    """상품을 장바구니에 추가"""
    # products 딕셔너리에서 상품의 가격을 가져옴
    for category in products.values():
        for name, price, _ in category:
            if name == product_name:
                if product_name in cart:
                    # 수량 증가
                    cart[product_name][0] += 1
                    # 단가 업데이트 (가격 변동이 있을 수 있으므로)
                    cart[product_name][1] = price
                    # 총 가격 업데이트
                    cart[product_name][2] = cart[product_name][0] * cart[product_name][1]
                else:
                    # 새로운 상품 추가 (수량, 단가, 총 가격)
                    cart[product_name] = [1, price, price]
                update_order_display()
                return



update_order_display()

root.mainloop()



