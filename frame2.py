import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox  


# 메인 윈도우 생성
second_window = tk.Tk()
second_window.title("상품 처리 화면")
second_window.geometry("700x800")  # 창 크기 설정



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
    fg="white", 
    command=process_order()
).pack(pady=10, padx=20, expand=True)

# 주문 처리 함수
def process_order():
    """주문 처리 로직 (추후 구현 예정)"""
    pass  # 현재는 구현 없음

second_window.mainloop()