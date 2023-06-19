# Import the following module
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL.ImageTk import PhotoImage
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from IPython.display import HTML
from base64 import b64encode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from threading import Thread
from tkinter import ttk, filedialog
import vehicle_crash_detection
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------------------------------Vehicle Crash Detector User Interface--------------------------------------------------------------------------------------
''' This class represents the user interface of the vehicle crash detector , it is called using the main class '''
class VcdUI:
    def __init__(self,root):
        self.root = root  # create root window
        self.root.state('zoomed')
        self.root.title(" Vehicle Crash Detector")
        self.root.config(bg="#ffaa00")

        self.title_bar_icon = PhotoImage(file="resources/icon/vehicle_crash_black.png")
        self.root.iconphoto(False, self.title_bar_icon)

        # create the main content frame
        self.content = tk.Frame(root, bg="#ffaa00", width=400)
        self.content.pack(side='right', fill='both', expand=True)

        # Load the image and resize it to the desired size
        self.icon_white = Image.open("resources/icon/vehicle_crash_white.png").resize((60, 60))
        self.icon_white = ImageTk.PhotoImage(self.icon_white)

        self.icon_black = Image.open("resources/icon/vehicle_crash_black._32.png").resize((60, 60))
        self.icon_black = ImageTk.PhotoImage(self.icon_black)

        self.title_label = tk.Label(self.content, text=" Vehicle Crash Detector", bg=root["bg"], font=('Cascadia Code Bold', 20),
                               fg="black", compound="left", image=self.icon_black)
        # Set the padding between the icon and text
        self.title_label.image = self.title_bar_icon
        self.title_label.pack(side="top", anchor="n", padx=10, pady=10)

        self.detections_update_label = tk.Label(self.content, text="", bg=root["bg"], font=('Cascadia Code Bold', 20),
                                           fg="white", )
        self.detections_update_label.pack(side="bottom", anchor="s", padx=10, pady=60)

        self.source = "No Video Source Provide Yet !"

        # create the sidebar container frame
        self.sidebar = tk.Frame(root, bg='#000000', width=25)
        self.sidebar.pack(side='left', fill='y')

        # Create a frame for the white border
        self.border_frame = tk.Frame(self.sidebar, bg='white', width=2)
        self.border_frame.pack(side='right', fill='y')

        # Create a Label widget to display the image
        self.sidebar_icon_label = tk.Label(self.sidebar, image=self.icon_white, bg='#000000')
        self.sidebar_icon_label.pack(side='top', pady=10)

        # create the buttons for sidebarcanvas items
        self.sidebar_button1 = tk.Button(self.sidebar, text='Crash Detection', width=25,height=2, fg="white", bg="#000000",
                                    font=('Cascadia Code', 10))
        self.sidebar_button1.pack()
        self.sidebar_button2 = tk.Button(self.sidebar, text='Records',command=self.open_image_viewer ,width=25,height=2 ,fg="white", bg="#000000",
                                    font=('Cascadia Code', 10)).pack()



        # Create a label for the combo box
        self.combo_label = tk.Label(self.content, text="Select a Video Source:", fg="white", bg=root["bg"],
                               font=('Cascadia Code', 12)).pack(side="top", anchor="n", padx=10, pady=10)
        self.combo_box = ttk.Combobox(self.content, values=["Video File", "Live-Camera"], text='Select an option')
        self.combo_box.pack(pady=10)

        # Bind the handle_combobox() function to the "<<ComboboxSelected>>" event
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_combobox)
        self.combo_box.pack(side="top", anchor="n", padx=10, pady=10)

        # Create a BooleanVar object
        self.var = tk.BooleanVar()

        # Create detection button
        self.button1 = tk.Button(self.content, text="Detection \nOFF", width=18, height=3, fg="white", bg="#000000",
                            command=self.toggle, font=('Cascadia Code', 9))
        self.button1.place(relx=0, rely=0.65, anchor="w", x=50, y=-150)

        # Create an instance of the vehicle_crash class
        self.vc = vehicle_crash_detection.VehicleCrash(self.detections_update_label, self.content, self.button1)
        # Call the load_model method on the instance
        self.vc.load_model()

    # function to open a file as video source
    def open_file(self):
        global source
        file_path = filedialog.askopenfilename()
        source = str(file_path)
        self.vc.set_source(source)
        return source

    # function to open a camera as video source
    def open_camera(self):
        global source
        source = 0
        self.vc.set_source(source)
        return source

    def handle_combobox(self,event):
        value = event.widget.get()
        if value == "Video File":
            self.open_file()
        elif value == "Live-Camera":
            self.open_camera()

    def clear_frame(self):
        keep_classes = [ttk.Combobox, tk.Button, tk.Label]
        for widget in self.content.winfo_children():
            if type(widget) not in keep_classes and type(widget.winfo_parent()) not in keep_classes:
                widget.destroy()

    def toggle(self):
        # Toggle the state of the variable
        self.var.set(not self.var.get())

        # Set the button text to "On" or "Off" depending on the state of the variable
        if self.var.get():
            self.button1.config(text="Detection \nON")

            self.vc.run_detection()
        else:
            self.button1.config(text="Detection \nOFF")
            self.vc.stop_detection()
            self.detections_update_label.configure(text="")
            self.clear_frame()

    def open_image_viewer(self):
        self.root.withdraw()  # hide the current window
        # Create a new window for the image viewer
        image_viewer_window = tk.Toplevel(self.root)
        image_viewer_window.title("Image Viewer")

        # Create an instance of the image_viewer class
        from image_data_viewer import ImageViewer
        image_viewer_instance = ImageViewer(image_viewer_window)


if __name__ == '__main__':
    root = tk.Tk()
    app = VcdUI(root)
    root.mainloop()



#The icon used in the Vehicle Crash Detector Application is taken from the below source
'''<a href="https://www.flaticon.com/free-icons/crash" title="crash icons">Crash icons created by Freepik - Flaticon</a>'''
