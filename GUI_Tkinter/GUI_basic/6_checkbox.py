from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

chkvar=IntVar() #chkvar에 int형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택해제 처리
chkbox.pack()

chkvar2=IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0:체크해제 , 1:체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()