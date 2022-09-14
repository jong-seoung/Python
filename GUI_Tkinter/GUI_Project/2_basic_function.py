from distutils.cmd import Command
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title ("image compositing")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5, pady=5)

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.",filetypes= (("PNG 파일","*.png"),("모든 파일","*.*")),initialdir="c:/")

    for file in files:
        list_file.insert(END, file)

# 선택 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로
def browse_dest_path():
    folder_selected=filedialog.askdirectory()
    if folder_selected is None: # 사용자가 취소를 누를때
        return 
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0, folder_selected)

#시작
def start():
    print("가로 넓이 : ", width_cmb.get())
    print("간격 : ", space_cmb.get())
    print("포맷 : ", format_cmb.get())
     
    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요.")
        return

    #저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고","저장 경로를 선택하세요.")
        return



btn_add_file = Button(file_frame, padx = 5, pady = 5, width =12, text="파일추가",command=add_file)
btn_add_file.pack(side="left")



btn_del_file = Button(file_frame, padx = 5, pady = 5, width =12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height= 15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로
path_frame = LabelFrame(root, text="저장경로",padx=5, pady=5)
path_frame.pack(fill="x", ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x",expand=True,padx=5, pady=5, ipady=4)

btn_dest_path= Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5, pady=5, ipady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션",padx=5, pady=5)
option_frame.pack()

# 가로 넓이 옵션
## 가로 넓이 레이블"
width_label = Label(option_frame, text="가로넓이", width=8)
width_label.pack(side="left",padx=5, pady=5)

## 가로 넓이 콤보
width_opt = ["원본유지","1024","800","640"]
width_cmb = ttk.Combobox(option_frame, state="readonly", values=width_opt, width= 8)
width_cmb.current(0)
width_cmb.pack(side="left",padx=5, pady=5)

#간격 옵션
## 간격 옵션 레이블
space_label = Label(option_frame, text="간격옵션", width=8)
space_label.pack(side="left",padx=5, pady=5, ipady=5)

## 가로 넓이 콤보
width_space = ["없음","좁게","보통","넓게"]
space_cmb = ttk.Combobox(option_frame, state="readonly", values=width_space, width= 8)
space_cmb.current(0)
space_cmb.pack(side="left",padx=5, pady=5)

# 파일 포맷 옵션
## 포맷 옵션 레이블
format_label = Label(option_frame, text="포맷옵션", width=8)
format_label.pack(side="left",padx=5, pady=5)

## 포맷 넓이 콤보
width_format = ["PNG","JPG","BMP"]
format_cmb = ttk.Combobox(option_frame, state="readonly", values=width_format, width= 8)
format_cmb.current(0)
format_cmb.pack(side="left",padx=5, pady=5)

#진행 상황 progress bar
progress_frame = LabelFrame(root, text="진행상황",padx=5, pady=5)
progress_frame.pack(fill="x",padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum=100, variable=p_var)
progress_bar.pack(fill="x")

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x",padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right",padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right",padx=5, pady=5)



root.resizable(False, False)
root.mainloop()