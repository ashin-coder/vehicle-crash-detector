# Import the following module
import threading
import time
from tkinter.ttk import Style
import PIL
import tensorflow as tf
import cv2
import numpy as np
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from IPython.display import HTML
from base64 import b64encode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from tkinter import ttk
import functools
import email_alert
import sms_alert
import datetime

# ---------------------------------------------------Vehicle Crash Detection--------------------------------------------------------------------------------------
''' This class represents the vehicle crash detector functionalities , it is called when using the vcd_ui class '''

class VehicleCrash:

    def __init__(self, detections_update_label, content, button1):
        self.detections_update_label = detections_update_label
        self.content = content
        self.source = None
        self.running = False
        self.button1 = button1
        self.count = 0
        self.i = 0

    def set_source(self, source):
        self.source = source

    PATH_TO_SAVED_MODEL = "inference_graph\\saved_model"

    category_index = label_map_util.create_category_index_from_labelmap("label_map.pbtxt",
                                                                        use_display_name=True)


   #visualise_on_image() is used to show label when an Vehicle Crash is detected
    def visualise_on_image(self, frame, image, bboxes, labels, scores, thresh):
        (h, w, d) = image.shape
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        for bbox, label, score in zip(bboxes, labels, scores):
            if score > thresh:
                xmin, ymin = int(bbox[1] * w), int(bbox[0] * h)
                xmax, ymax = int(bbox[3] * w), int(bbox[2] * h)

                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                cv2.putText(image, f"{label}: {int(score * 100)} %", (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)

                self.count += 1
                print(self.count)

                if (self.count == 5):
                    label_box_image = frame[ymin:ymax, xmin:xmax]
                    cv2.imwrite("outputs/frame_img/vcd_frame" + str(current_datetime) + str(self.i) + ".jpg", image)
                    # Define the desired image size
                    image_size = (1920, 1080)  # width, height

                    # Resize the image to the desired size
                    resized_image = cv2.resize(label_box_image, image_size)

                    # Apply a sharpening filter to the resized image
                    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])  # 3x3 sharpening filter
                    sharpened_image = cv2.filter2D(resized_image, -1, kernel)

                    # Save the sharpened image with high quality
                    png_quality = 100
                    cv2.imwrite("outputs/inside_label_img/vcd_inlabel" + str(current_datetime) + str(self.i) + ".png",
                                sharpened_image,
                                [int(cv2.IMWRITE_JPEG_QUALITY), png_quality])

                if (self.count == 20):
                    # Save the image inside the label box
                    # self.detections_update_label.configure(text="Vehicle Crash has been Detected")
                    print("Vehicle_Crash_Detected")
                    perform_label_detected_func = threading.Thread(target=self.perform_label_detected)
                    perform_label_detected_func.start()
                    self.i += 1
                    self.count = 0
                    break

        # Reset the count variable after the loop has completed
        return image

    # update progress() used to update value progress bar when loading the model
    def update_progress(self, progress, value):
        progress['value'] = value
        progress.update()

    # perform_label_detected() function performs certain activities including
    # functioning of alert systems when vehicle crash is detected
    def perform_label_detected(self):
        self.detections_update_label.configure(text="Vehicle Crash has been Detected")
        em = email_alert.Email(self.source)
        em.run_mail()
        self.detections_update_label.configure(
            text="Email Alert Send Successfully to nearby Hospital,Police Station and RTO")
        time.sleep(0.5)
        sm = sms_alert.Sms(self.source)
        sm.run_sms()
        self.detections_update_label.configure(
            text="SMS Alert Send Successfully to nearby Hospital,Police Station and RTO")
        time.sleep(0.5)
        self.detections_update_label.configure(
            text="Email and SMS Alert Send Successfully to nearby Hospital,Police Station and RTO")
        time.sleep(0.5)
        self.detections_update_label.configure(text="")

    detect_fn = ""

    @functools.lru_cache(maxsize=None)
    # load_model() function loads the model when the application is started
    def load_model(self):

        style = Style()
        style.theme_use('alt')
        # Self test for each subject,'winnative','clam','alt','default','classic' Test successful.
        # windows theme:('winnative','clam','alt','default','classic','vista','xpnative')
        style.configure("Horizontal.TProgressbar", troughcolor='white', background='black', thickness=30)

        # create a progress bar
        progress = ttk.Progressbar(self.content, orient=tk.HORIZONTAL, style="Horizontal.TProgressbar", length=300,
                                   mode='determinate')
        progress.pack(pady=200, side="top", anchor="s")
        self.detections_update_label.configure(text="Loading 0%")
        self.update_progress(progress, 0)
        time.sleep(0.1)

        print("Loaded 10% saved model ...")
        self.update_progress(progress, 10)
        self.detections_update_label.configure(text="Loading .10%")
        time.sleep(0.1)

        global detect_fn
        print("Loading saved model ...")

        detect_fn = tf.saved_model.load(self.PATH_TO_SAVED_MODEL)
        print("Loaded 50% saved model ...")
        self.detections_update_label.configure(text="Loading ....50%")
        self.update_progress(progress, 50)
        time.sleep(1.5)

        print("Model Loaded!")
        self.detections_update_label.configure(text="Loading .........100%")
        self.update_progress(progress, 100)
        time.sleep(1.5)
        self.detections_update_label.configure(text="")
        time.sleep(0.1)
        progress.destroy()
        return detect_fn

    # close_canvas() is used to close the canvas which displays the detection from the video source
    def close_canvas(self, canvas):
        canvas.destroy()
        self.content.update()

    # run_detection function is called when detection button is clicked ,
    # it is used to detect the occurrence of vehicle crash from the given video source
    def run_detection(self):
        self.running = True
        while self.running:

            print("Video Source : ", self.source)
            video_capture = cv2.VideoCapture(self.source)

            start_time = time.time()
            canvas = tk.Canvas(self.content, width=1000, height=600)
            canvas.pack(side="top", anchor="n", padx=10, pady=40)

            frame_width = int(video_capture.get(3))
            frame_height = int(video_capture.get(4))
            # fps = int(video_capture.get(5))
            size = (frame_width, frame_height)
            # Initialize video writer
            result = cv2.VideoWriter('outputs/detection_video/det_vid.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                                     15,
                                     size)

            while True:
                ret, frame = video_capture.read()
                if not ret:
                    self.close_canvas(canvas)
                    self.stop_detection()
                    self.button1.config(text="Detection \nOFF")
                    self.detections_update_label.configure(text="")
                    self.source = "Video Source"
                    print('Unable to read video / Video ended')
                    self.detections_update_label.configure(text="Unable to read video / Video ended")
                    break

                frame = cv2.flip(frame, 1)
                image_np = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
                # The model expects a batch of images, so also add an axis with `tf.newaxis`.
                input_tensor = tf.convert_to_tensor(image_np)[tf.newaxis, ...]

                # Pass frame through detector
                detections = detect_fn(input_tensor)

                # Set detection parameters
                score_thresh = 0.92  # Minimum threshold for object detection
                max_detections = 1

                # All outputs are batches tensors.
                # Convert to numpy arrays, and take index [0] to remove the batch dimension.
                # We're only interested in the first num_detections.
                scores = detections['detection_scores'][0, :max_detections].numpy()
                bboxes = detections['detection_boxes'][0, :max_detections].numpy()
                labels = detections['detection_classes'][0, :max_detections].numpy().astype(np.int64)
                labels = [self.category_index[n]['name'] for n in labels]

                # Display detections
                self.visualise_on_image(frame, frame, bboxes, labels, scores, score_thresh)
                # Convert the frame to a Tkinter-compatible format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = PIL.Image.fromarray(frame)
                image = image.resize((1000, 600))
                photo = PIL.ImageTk.PhotoImage(image)

                # Perform Certain Functions on Detections
                # perform_label_detected(labels, scores, score_thresh)
                end_time = time.time()
                fps = int(1 / (end_time - start_time))
                start_time = end_time

                # Update the canvas with the new frame and text
                canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                canvas.create_text(50, video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 25, text=f"FPS: {fps}",
                                   font=("Arial", 14), fill="red", anchor=tk.NW)
                canvas.update()

                # Write output video
                result.write(frame)
            video_capture.release()

    # stop_detection() function is called to end an already running run_detection function ,it is called by clicking the
    # detection button again while running run_detection for  Vehicle Crash Detection
    def stop_detection(self):
        self.running = False
        self.count = 0
        print("Detection Stopped")
