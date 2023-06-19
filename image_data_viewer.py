# Import the following module
import os
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from PIL.ImageTk import PhotoImage
from tkinter import ttk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#-------------------------------------------------- Image Viewer (Records) ----------------------------------------------------------------#
''' This class is used to view Image Records of Vehicle Crash which is saved locally when a Vehicle Crash is detected '''

class ImageViewer:
    def __init__(self,root):
        self.root =root
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

        # Create a menu bar
        self.menu_bar = tk.Menu(root, background='blue', fg='white')
        self.root.config(menu=self.menu_bar)

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
        self.sidebar_button1 = tk.Button(self.sidebar, text='Crash Detection',command=self.open_vcd ,width=25,height=2 ,fg="white", bg="#000000",
                                    font=('Cascadia Code', 10)).pack()
        self.sidebar_button2 = tk.Button(self.sidebar, text='Records', width=25,height=2, fg="white", bg="#000000",
                                    font=('Cascadia Code', 10)).pack()

        # Create a label for the combo box
        self.combo_label = tk.Label(self.content, text="Select the Image Folder:", fg="white", bg=root["bg"],
                               font=('Cascadia Code', 12)).pack(side="top", anchor="n", padx=10, pady=10)
        self.combo_box = ttk.Combobox(self.content, values=["Frame Images", "Inside Label Images"], text='Select an option')
        self.combo_box.pack(pady=10)

        # Bind the handle_combobox() function to the "<<ComboboxSelected>>" event
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_combobox)
        self.combo_box.pack(side="top", anchor="n", padx=10, pady=10)


        self.images_list = []
        self.image_filenames = []
        self.index = 0

        # Create a placeholder image
        self.placeholder_img = Image.new("RGB", (1000, 600), "#ffaa00")
        self.placeholder_photo = ImageTk.PhotoImage(self.placeholder_img)

        self.canvas = tk.Canvas(self.content, width=1000, height=600, highlightthickness=0)
        self.canvas.pack(side="top", anchor="n", padx=10, pady=40)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.placeholder_photo)

        # Create two buttons
        self.next_button = tk.Button(self.content, text="Next Image", command=lambda: self.next(0), width=18, height=3, fg="white",
                                bg="#000000", font=('Cascadia Code', 9))
        self.next_button.place(relx=0, rely=0.5, anchor="w", x=50, y=-150)

        self.back_button = tk.Button(self.content, text="Previous Image", width=18, height=3, command=lambda: self.next(0),
                                fg="white", bg="#000000", font=('Cascadia Code', 9))
        self.back_button.place(relx=0, rely=0.65, anchor="w", x=50, y=-150, )

    def handle_combobox(self, event):

        value = event.widget.get()
        if value == "Frame Images":
            source = "outputs/frame_img"
            self.set_img_directory(source)
            self.detections_update_label.config(text="Folder : " + source)
            self.refresh_canvas()
        elif value == "Inside Label Images":
            source = "outputs/inside_label_img"
            self.set_img_directory(source)
            self.detections_update_label.config(text="Folder : " + source)
            self.refresh_canvas()

    # #tkinter file ends here
    # self.root.mainloop()

    # Define a function to open a file
    def frame_img(self):

        file_path = "outputs/frame_img"
        source = str(file_path)
        return source

    def inside_label_img(self):

        file_path = "outputs/inside_label_img"
        self.source = str(file_path)
        return self.source

    def refresh_canvas(self):
        self.canvas.update()
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.placeholder_photo)

    def set_img_directory(self, source):

        self.images_list.clear()
        self.image_filenames.clear()
        # Get a list of all image files in the directory
        for filename in os.listdir(source):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Open the image and create a PhotoImage object
                image = Image.open(os.path.join(source, filename))
                image = image.resize((1000, 600), resample=Image.LANCZOS)
                photo_image = ImageTk.PhotoImage(image)
                self.images_list.append(photo_image)
                self.image_filenames.append(filename)

    def next(self, index):


        if index == len(self.images_list) - 1:
            return
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.images_list[index + 1])
        self.detections_update_label.config(text="Image File : " + self.image_filenames[index + 1])

        # Create two buttons
        next_button = tk.Button(self.content, text="Next Image", command=lambda: self.next(index + 1), width=18, height=3,
                                fg="white",
                                bg="#000000", font=('Cascadia Code', 9))
        next_button.place(relx=0, rely=0.5, anchor="w", x=50, y=-150)
        back_button = tk.Button(self.content, text="Previous Image", width=18, height=3,
                                command=lambda: self.back(index + 1),
                                fg_="white", bg="#000000", font=('Cascadia Code', 9))
        back_button.place(relx=0, rely=0.65, anchor="w", x=50, y=-150, )

        return

    def back(self, index):


        if index == 0:
            return
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.images_list[index - 1])
        self.detections_update_label.config(text="Image File : " + self.image_filenames[index - 1])

        # Create two buttons
        next_button = tk.Button(self.content, text="Next Image", command=lambda: self.next(index - 1), width=18, height=3,
                                fg="white",
                                bg="#000000", font=('Cascadia Code', 9))
        next_button.place(relx=0, rely=0.5, anchor="w", x=50, y=-150)
        back_button = tk.Button(self.content, text="Previous Image", width=18, height=3,
                                command=lambda: self.back(index - 1),
                                fg_="white", bg="#000000", font=('Cascadia Code', 9))
        back_button.place(relx=0, rely=0.65, anchor="w", x=50, y=-150, )

        return

    def open_vcd(self):
        self.root.withdraw()  # hide the current window
        # Create a new window for the image viewer
        vcd_window = tk.Toplevel(self.root)
        vcd_window.title("VCD")

        # Create an instance of the image_viewer class
        from vcd_ui import VcdUI
        vcd_instance = VcdUI(vcd_window)



if __name__ == '__main__':
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()


