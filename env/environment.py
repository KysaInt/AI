import pyautogui
import mss
import time
import numpy as np
import cv2

# 设置你游戏窗口的位置
monitor = {"top": 97, "left": 1860, "width": 256, "height": 220}

def press_key(key, duration=0.1):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def grab_screen():
    with mss.mss() as sct:
        img = np.array(sct.grab(monitor))
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

if __name__ == "__main__":
    # 抓一张图看看
    img = grab_screen()
    cv2.imshow("Game", img)
    cv2.waitKey(1000)

    # 模拟按下Z（对应游戏的A键）
    press_key("z")