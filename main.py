from tkinter import *
import pyautogui
import random
from pathlib  import Path

x = 1400
cycle = 0
check = 1
idle_num = [1,2,3,4];
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = str(Path(__file__).parent.resolve())
print(impath)

window = Tk()

#idle = [PhotoImage(file=impath+'/GIF/xiao_whistling.gif',format = 'gif -index %i' %(i)) for i in range(3)]
#window.config(highlightbackground='black')
#window.overrideredirect(True)
#window.wm_attributes('-alpha','0.5')
#label = Label(window,bd=0,bg='black')
#label.pack()
window.mainloop()