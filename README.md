<h1 align="center" id="title">Vehicle Crash Detector</h1>

https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/063a5a2a-3d0d-4f98-94d0-967e9fb36596

The Vehicle Crash Detector is an innovative project that aims to enhance road safety by actively detecting Vehicle Crash Accidents on the road using CCTV footage and alert mechanisms. The system employs object detection technology based on TensorFlow to accurately identify accidents involving vehicle crashes and promptly notify the nearest hospitals police stations and RTO with detailed accident information. The core of the system relies on CCTV data as a source to function The Vehicle Crash Detector project is a Vehicle Crash Detection and Alert System which could be integrated with existing systems. By leveraging video surveillance systems the focus of this system is to actively detect vehicle crash accidents and promptly respond to ensure the safety of individuals involved. The system utilizes advanced detection algorithms for crash detection based on TensorFlow which enables it to identify vehicle crashes in real time. By analysing the CCTV footage the system can detect potential accidents involving vehicle crashes. When an accident is detected the system captures a snapshot of the accident scene and generates an alert in the form of Email and SMS with necessary information. Upon detection, the Vehicle Crash Detector automatically notifies the nearest hospitals, police stations and RTO providing them with the accident location snapshot and initial details about the vehicle crash accident. This rapid alert mechanism ensures that emergency services can be dispatched promptly to the accident location potentially reducing response times and improving the chances of saving lives. Overall the Vehicle Crash Detector offers a comprehensive solution to enhance road safety through proactive accident detection and swift response. By leveraging CCTV technology, advanced algorithms and integration with emergency services the system aims to minimize the impact of vehicle crash accidents and provide timely assistance to those in need.

## Installation

1. Clone the repository: git clone https://github.com/ashin-coder/vehicle-crash-detector.git
2. Install Python (version 3.10 or Other Versions may work depending on compatibility) from the official website: Python
3. Install a Python IDE preferably PyCharm to prevent any kind of incompatibilities since this project was developed in PyCharm
4. Install the required dependencies using pip: pip install "dependency name" ( check the imports in the code)
5. Run the Application from the main.py file in the IDE

**Please Note**: As Mentioned before this installation is based on "PyCharm" IDE as it was developed in the same, Project may or may not work as expected in Other IDEs. Also, an Internet Connection is required for the alert system implemented in the application to function

## Features

* The System offers the option to detect vehicle crashes either by analyzing video files of past incidents or using live camera feeds for real-time detection.
* Automatically generates alerts with Vehicle Crash Accident details in the form of Email and SMS
* In the event of an incident, specific emails are sent to Hospitals, Police Stations, and RTO based on the respective services they can provide to address the situation promptly and effectively.
* After detecting an accident, the system captures a snapshot that can be viewed in the application's records section. It includes a frame image of the accident scene and a labelled image indicating the vehicles involved.
* The GUI makes the application user-friendly and easy to use.

## Implementation

The Project utilizes Python, OpenCV, and TensorFlow 2 to develop  and run the Vehicle Crash Detection model. Python is a high-level programming language known for its versatility and is widely used in artificial intelligence and data science. OpenCV is a popular open-source library specifically designed for computer vision, providing a comprehensive set of tools for image and video analysis. TensorFlow 2, developed by Google, is an open-source machine learning framework that enables the creation and deployment of deep learning models, offering flexibility and scalability. Together, these technologies form a powerful combination for building and training advanced computer vision models. 

To train the Vehicle Crash Detection model using the TensorFlow Object Detection API, the first step is to collect a dataset of vehicle crash accident images and manually label them, creating corresponding XML files containing the bounding box coordinates and class labels for each object. Once the dataset is prepared, the next step involves installing the TensorFlow Object Detection API, which provides a framework for training and deploying object detection models. After installation, it is necessary to generate the TFRecord files, which are binary files containing the labelled image data and annotations. This is done using the provided script called generate_tfrecord.py, along with CSV files that map the class labels to numerical IDs. The generated TFRecord files are required for training the model. Following this, the model pipeline configuration file needs to be edited to specify the model architecture, training parameters, and paths to the TFRecord files. Additionally, a pre-trained model checkpoint can be downloaded from the TensorFlow Model Zoo and used as a starting point for training. Finally, the model can be trained and evaluated using the configured pipeline. This involves feeding the TFRecord files into the training process, which optimizes the model's parameters to learn the object detection task and evaluate its performance on a separate validation set.

The model used here is trained using a dataset consisting of 4000+ images of vehicle crash accidents sourced from the internet which are manually labelled, a batch size of 32 and 50000 was taken as the number of steps to train using TensorFlow 2. OpenCV with GPU acceleration was used to run the model in the project which allows for efficient and high-speed processing of computer vision tasks, leveraging the parallel processing capabilities of GPUs to significantly enhance performance and enable real-time video analysis. The model developed is used in the application and it's successful in detecting vehicle crashes from videos provided to it through the application interface as the source. Once the Vehicle Crash is Detected, the user will be notified about the detection of the vehicle crash and an alert message being sent in the application window. The Detection model was trained based on the learning from the YouTube tutorials provided by TechZizou. The specific tutorial can be found at the following link: [YouTube Tutorial](https://www.youtube.com/watch?v=amURyS6CAaY&ab_channel=techzizou). For further information and resources, you can visit TechZizou's website at [TechZizou Website](https://www.techzizou.com).

The automated Alert Message will be sent in the form of SMS and Email to the emergency services in this case Hospital, Police Station and RTO. SMS messages send to them would contain initial information regarding the vehicle crash accident. Each Department will receive specific emails based on the services provided by them and these email contents are written in external text files. The emails will contain initial information regarding the vehicle crash accident which include location, time, image from the vehicle crash site etc. Here API used for SMS service is provided by fast2sms and the Email service is provided by Gmail.

The Vehicle Crash Detector saves images of the crash detected locally which could be viewed from the application itself from Records Section. The Graphical User Interface in the Application is developed using Tkinter. It makes the application easy to use and user-friendly.

**Please Note**: The Alert System will not work without setting up SMS and Email APIs with the necessary credentials. for further information visit 

https://www.fast2sms.com/

https://developers.google.com/gmail/api/guides

## Project Screenshots

* Vehicle Crash Detector Home Page
![vcd_demo_img_1](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/37d132b3-e1ca-4756-85cf-4441afa4a990)

* Vehicle Crash Detector Records Page
![vcd_demo_img_2](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/496521a0-11b2-4389-a37d-af2d4eb69f8b)

* SMS Alert
![sms_alert](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/5d4e3a18-ff07-451f-9005-cfbbc9427dce)

* Email Alert (Hospital)
![hospital_email](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/5e5a752d-c931-4dc1-b859-369d34226864)
* Email Alert (Police Station)
![police_station_email](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/24ee976b-03b3-4873-8c90-3826a6ee52a2)
* Email Alert (RTO)
![rto_email](https://github.com/ashin-coder/vehicle-crash-detector/assets/73836674/358f33e4-0d8d-425e-90e1-c6ec19fc836c)

## Contributors

I would like to acknowledge and express my gratitude to the following individuals including me who contributed to the development of this project:
* Ashin Kunjumon ([@ashin-coder](https://github.com/ashin-coder))
* Athul Roy ([@stig777m](https://github.com/stig777m))
* Meena Thamban

I sincerely appreciate their time, effort, and dedication in making this project a reality. Without their invaluable contributions, this project would not have been possible.

## Acknowledgments

We would like to thank the developers and contributors of Python, as well as the libraries and frameworks used in this project, for providing the tools and resources and also those who provided the knowledge and support to make this Vehicle Crash Detector project possible. The icon used in this project was sourced from Flaticon, a platform for high-quality icons. I appreciate the creator of the icon for their work

## Limitations

**Please Note**: The Accuracy of the Vehicle Crash Detection model employed in the project hinges on various essential factors. The effectiveness of this model is influenced by the quality of the training data and its ability to handle real-world scenarios. While efforts have been made to train the model using a diverse set of images featuring vehicle crashes from different angles, varying visibility, and image quality, it is important to note that we cannot guarantee that the model will successfully detect crashes in all video sources. It is crucial to acknowledge that the system may encounter limitations in accurately detecting certain types of crashes due to different inherent constraints.

Moreover, the reliability of the Vehicle Crash Detector is closely tied to the availability and quality of the CCTV footage it relies upon. The system analyses this footage to identify potential crashes in real time. However, limited coverage or low-quality footage can hamper the system's effectiveness, potentially leading to missed or misidentified crashes. In terms of hardware requirements, GPU acceleration is often recommended for real-time video analysis in crash detection systems. The use of compatible hardware with GPU acceleration can significantly enhance the system's performance and response time. Conversely, running the system without GPU acceleration may result in decreased efficiency and slower detection capabilities. It is advised to use OpenCV with GPU for smoother functioning of the project

## Project Disclaimer: For Demonstration Purposes Only

**Please Note**: The project provided here is for demonstration purposes only and may contain bugs or glitches. It is important to understand that this implementation may require further development and refinement before it can be considered suitable for real-world applications. The intention behind sharing this project is to provide a starting point and showcase the potential of the concepts and technologies used. It is encouraged for users to further enhance and improve the project based on their specific needs and requirements.

Feel free to contribute, modify, or build upon this project to make it better and more robust. Your feedback, bug reports, and suggestions for improvement are highly appreciated. 

## Note on Data Used in the Project Implementation

**Please Note**: The data which includes test videos, project resources and other information used in this project is solely intended for demonstration purposes and is not owned by the project contributors. It is important to acknowledge that some of the data utilized may not be accurate or up to date and also include data sourced from the internet. It is essential to exercise caution when interpreting or relying on the information presented in Project Implementation.
We strongly encourage users to seek authorized and reliable sources for the most accurate and current data in their respective fields. The purpose of this project is to showcase the functionality and capabilities of the Application, and it should not be considered a reliable source of data.

