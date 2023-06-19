# Import the following module
import vcd_ui
import tkinter as tk

# --------------------------------------------------- Run Vehicle Crash Detector Application--------------------------------------------------------------------------------------
''' This is the main file of the Vehicle Crash Detector Application used for running the Application '''
root = tk.Tk()
app = vcd_ui.VcdUI(root)
root.mainloop()