import pyautogui

# file_menu = pyautogui.locateOnScreen("Desktop//file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 화면 해상도, 이미지가 변경되면 오류가 날 가능성이 매우 높음

# 화면에 중복되는 이미지가 여러개 있을 경우 처리법
# for i in pyautogui.locateAllOnScreen("Desktop//file_menu.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# 처음 나오는 이미지만 클릭하고 넘어가는 법
# check_box = pyautogui.locateOnScreen("Desktop//file_menu.png")
# pyautogui.click(check_box)

### 속도 개선
# 1. GrayScale - 흑백으로 만든 후 탐색 
# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png", grayscale=True) # 정확도는 떨어질 수 있음
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png", region=x,y,width,height) # 탐색 시작 위치 x,y
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 ## pip install opencv-python 설치 필요
run_btn = pyautogui.locateOnScreen("Desktop//run_btn.png", confidence=0.9) #90퍼센트이상 일치하면 작동
pyautogui.moveTo(run_btn)