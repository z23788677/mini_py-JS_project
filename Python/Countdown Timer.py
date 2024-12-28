from tkinter import *
import time as t

win = Tk()
win_size_width = 400
win_size_height = 400
win_size_user_width_info = int(win.winfo_screenwidth() / 2) - int(win_size_width/2)
win_size_user_height_info = int(win.winfo_screenheight() / 2) - int(win_size_height/2)

win.geometry(f"{win_size_width}x{win_size_height}+{win_size_user_width_info}+{win_size_user_height_info}")

enter_time = Entry(font="微軟正黑體",text = "Time_countdown")
enter_time.grid(0,0)

win.mainloop()