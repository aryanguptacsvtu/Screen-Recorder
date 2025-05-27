import cv2
import pyautogui
import numpy as np  
import time
from win32api import GetSystemMetrics


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim =(width, height)

f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", f, 20.0, dim)

start_time = time.time()
dur = int(input("Enter duration (in seconds): "))
end_time = start_time + dur

print("🎥 Recording...")
print("🛑 Press Ctrl+C to stop recording.")

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    curr_time = time.time()
    if curr_time > end_time:
        break

output.release()
print("Video Recorded Successfully✅")