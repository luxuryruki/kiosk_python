import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox  


# 메인 윈도우 생성
root = tk.Tk()
root.title("상품 주문 화면")
root.geometry("1400x800")  # 창 크기 설정

# 예시 데이터
ready_list = []  # 준비완료 리스트
pending_list = []  # 준비중 리스트
cart = {} 
order_number = 100

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
    for product_name, (quantity, price) in cart.items():
        frame = tk.Frame(order_list, bg="white")
        frame.pack(fill="x", pady=5)

        # 왼쪽: 상품명 표시
        tk.Label(frame, text=f"{product_name}", font=("Arial", 20), bg="white", anchor="w").pack(side="left", padx=5)

        # 오른쪽: 수량 조정 버튼 및 수량 표시
        controls_frame = tk.Frame(frame, bg="white")
        controls_frame.pack(side="right", padx=10)

        # + 버튼
        tk.Button(
            controls_frame, text="+", font=("Arial", 20), command=lambda p=product_name: update_quantity(p, 1)
        ).pack(side="left", padx=2)

        # 수량 표시    
        tk.Label(controls_frame, text=f"{quantity}", font=("Arial", 20), bg="white").pack(side="left", padx=5)
        
        # - 버튼
        tk.Button(
            controls_frame, text="-", font=("Arial", 20), command=lambda p=product_name: update_quantity(p, -1)
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
    update_order_display()


def place_order():
    """주문 처리"""
    global order_number  # 주문 번호를 전역 변수로 사용

    if cart:  # 장바구니에 상품이 있는 경우에만 처리
        # 주문 완료 메시지
        messagebox.showinfo(
            "주문 완료",
            f"주문이 완료되었습니다!\n주문번호: {order_number}"
        )

        # 주문 번호를 대기 목록에 추가
        pending_list.append(order_number)

        # 주문 번호 증가
        order_number += 1

        # 장바구니 초기화 및 UI 업데이트
        cart.clear()
        update_order_display()
        update_pending_display()
    else:
        # 장바구니 비어 있을 때 경고 메시지
        messagebox.showwarning("장바구니 비어 있음", "장바구니가 비어 있습니다. 주문을 추가하세요.")

def update_pending_display():
    """하단 준비 중 영역 UI 업데이트"""
    # 기존 위젯 삭제
    for widget in lower_frame.winfo_children():
        widget.destroy()

    # '준비중' 제목 표시
    tk.Label(lower_frame, text="준비중", font=("Arial", 24), width=20, height=2, bg="white").pack(pady=10)

    # 대기 중인 주문 번호 표시
    if pending_list:
        pending_numbers = ", ".join(map(str, pending_list))  # 리스트를 문자열로 변환
        tk.Label(lower_frame, text=pending_numbers, font=("Arial", 20), anchor="w", bg="white").pack(pady=10, padx=10, fill="x")
    else:
        # 대기 중인 주문이 없을 때 메시지 표시
        tk.Label(lower_frame, text="대기 중인 주문이 없습니다.", font=("Arial", 20), bg="white").pack(pady=10)


def add_to_cart(product_name):
    """상품을 장바구니에 추가"""
    # 장바구니에 상품이 이미 있는 경우 수량 증가
    if product_name in cart:
        cart[product_name][0] += 1  # 수량 증가
        update_order_display()
    else:
        # 상품을 처음 추가하는 경우, 초기 수량은 1
        # products 딕셔너리에서 상품의 가격을 가져옴
        for category in products.values():
            for name, price, _ in category:
                if name == product_name:
                    cart[product_name] = [1, price]  # 초기 수량 1, 가격 추가
                    update_order_display()


update_order_display()
root.mainloop()



