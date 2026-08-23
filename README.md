🎯 AI Object Detection & Tracking

<p align="center">
  <img src="./AI OBJECT.png" width="100%" alt="AI Object Detection & Tracking Banner">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/YOLO-Object%20Detection-purple?style=for-the-badge" alt="YOLO">
  <img src="https://img.shields.io/badge/DeepSORT-Object%20Tracking-orange?style=for-the-badge" alt="DeepSORT">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

<p align="center">
  <b>🤖 Intelligent Object Detection, Tracking & Video Analytics System</b>
</p>

<p align="center">
  Developed as part of the <b>DecodeLabs AI Internship — Task 4</b>
</p>

<p align="center">
  <a href="https://ai-object-detection-tracking-xoydqolhfxgcxmvefv45ac.streamlit.app/">
    🚀 <b>View Live Demo</b>
  </a>
</p>

📌 About the Project

AI Object Detection & Tracking is a Computer Vision application that detects, tracks, and analyzes objects in uploaded videos using YOLO and DeepSORT.

The system processes videos frame-by-frame, detects objects, assigns unique tracking IDs, visualizes movement trajectories, generates real-time statistics and alerts, and produces final analytics and tracking reports.

The application is built with an interactive Streamlit dashboard, allowing users to upload videos, adjust detection settings, filter object classes, monitor tracking information, view trajectories, analyze results, and download the processed video.

🎓 Internship Project: DecodeLabs AI Internship — Task 4

🚀 Live Demo

<p align="center">
  <a href="https://ai-object-detection-tracking-xoydqolhfxgcxmvefv45ac.streamlit.app/">
    🔗 <b>Try AI Object Detection & Tracking Live</b>
  </a>
</p>

The application is deployed using Streamlit Community Cloud.

✨ Key Features

🤖 Detection & Tracking

YOLO real-time object detection

DeepSORT multi-object tracking

Unique ID assignment

People detection and tracking

Vehicle detection and tracking

Object class filtering

Adjustable confidence threshold

📍 Movement Analysis

Object tracking paths

Adjustable trajectory length

Current and previous object positions

Movement trajectory visualization

🚨 Alerts & Monitoring

Live detection alerts

Person detection alerts

Vehicle detection alerts

Configurable object-limit alerts

Detection alert log

📊 Analytics & Reports

Live object statistics

Unique object counts

Unique people and vehicle counts

Detection counts by class

Maximum objects per frame

Processing FPS

Processing time

Detection charts

Detailed tracking report

🎥 Video Processing

Original video preview

Processed video preview

Frame-by-frame processing

Bounding boxes and labels

Object IDs

Tracking trajectories

Downloadable processed video

📁 Supported Video Formats

MP4 • AVI • MOV • MKV

🧠 How It Works

📁 Upload Video
       ↓
🎥 Read Video Frames
       ↓
🤖 YOLO Object Detection
       ↓
🎚️ Confidence Filtering
       ↓
🎯 Object Class Filtering
       ↓
🔍 DeepSORT Tracking
       ↓
🆔 Assign Unique Object IDs
       ↓
📍 Track Object Movement
       ↓
📊 Generate Live Statistics
       ↓
🚨 Generate Detection Alerts
       ↓
📈 Generate Analytics
       ↓
📋 Generate Tracking Report
       ↓
🎥 Create Processed Video
       ↓
⬇️ Download Result

🛠️ Technology Stack

Technology

Purpose

🐍 Python 3.12

Application development

🤖 YOLO

Real-time object detection

🔍 DeepSORT

Multi-object tracking

👁️ OpenCV

Computer vision & video processing

🎈 Streamlit

Interactive web application

📊 Pandas

Data processing & analytics

🔢 NumPy

Numerical processing

🐙 Git & GitHub

Version control

☁️ Streamlit Community Cloud

Deployment

🎯 Supported Object Categories

The system supports common object classes such as:

👤 Person

🚗 Car

🚌 Bus

🚚 Truck

🏍️ Motorcycle

🚲 Bicycle

🐕 Dog

🐈 Cat

🐦 Bird

The actual detected classes depend on the selected YOLO model and uploaded video.

👤 People Detection

The system can detect and track people throughout an uploaded video.

For each confirmed person, the application can display:

👤 Person class

🆔 Unique tracking ID

📦 Bounding box

📍 Movement trajectory

🎯 Detection confidence

🚨 Detection alerts

The application also calculates the number of unique people detected throughout the video.

🚗 Vehicle Detection

The system supports multiple vehicle categories, including:

🚗 Car

🚌 Bus

🚚 Truck

🏍️ Motorcycle

🚲 Bicycle

Vehicles receive tracking IDs and are included in analytics and tracking reports.

📍 Object Tracking & Trajectories

DeepSORT maintains object identities across video frames and stores previous object positions to visualize movement.

🆔 Object ID
     ↓
📍 Current Position
     ↓
📍 Previous Position
     ↓
💾 Store Tracking Points
     ↓
📈 Draw Movement Trajectory

This makes it easier to understand how objects move through the scene.

🚨 Intelligent Alerts

The application includes an alert system that monitors detected objects during processing.

Possible events include:

👤 Person detection

🚗 Vehicle detection

⚠️ Object-limit conditions

🔔 Detection events

The dashboard provides both Live Alerts and a Detection Alert Log.

📊 Live Statistics

During video processing, the dashboard displays real-time information such as:

Statistic

Description

🎯 Current Objects

Objects currently visible

👤 People

Current people detected

🚗 Vehicles

Current vehicles detected

⚡ Processing FPS

Current processing speed

📈 Final Analytics

After processing, the application generates final statistics including:

🆔 Unique objects

👤 Unique people

🚗 Unique vehicles

⏱️ Processing time

🎯 Maximum objects per frame

🔢 Detection events

⚡ Average processing FPS

🎚️ Detection Settings

The sidebar provides controls for customizing detection.

Confidence Threshold

Users can choose the minimum confidence required for a detection.

0.10 ─────────────── 0.50 ─────────────── 0.95

A higher threshold generally produces fewer but more confident detections.

Preview Every N Frames

Controls how frequently processed frames are displayed in the Streamlit interface, helping reduce UI overhead.

Object Filter

Users can select which object classes should be tracked.

Example:

☑ Person
☑ Car
☑ Bus
☑ Truck
☑ Motorcycle
☑ Bicycle

📹 Video Information

Before processing, the application displays information about the uploaded video:

📐 Resolution

🎞️ Video FPS

🎬 Total frames

⏱️ Duration

Example:

Resolution: 768 × 432
Video FPS: 12.0
Total Frames: 596
Duration: 49.7 seconds

ℹ️ Actual values depend on the uploaded video.

📄 Detailed Tracking Report

The application provides detailed tracking information that can include:

🆔 Object ID

🎯 Object class

🔢 Detection count

📍 Tracking information

🚨 Alert information

⏱️ Processing information

This makes the project useful for basic video surveillance, monitoring, and analytics scenarios.

📂 Project Structure

AI-Object-Detection-Tracking/
│
├── app.py
├── requirements.txt
├── yolov8n.pt
├── AI OBJECT.png
├── README.md
├── .gitignore
│
└── Screenshots/
    ├── Home.PNG
    ├── Detaction.PNG
    ├── detection.png
    ├── analytics.PNG
    └── process video.PNG

📸 Screenshots

🏠 Home Page

<p align="center">
  <img src="./Screenshots/Home.PNG" width="90%" alt="Home Page">
</p>

🎯 Object Detection

<p align="center">
  <img src="./Screenshots/Detaction.PNG" width="90%" alt="Object Detection">
</p>

📊 Detection Results

<p align="center">
  <img src="./Screenshots/detection.png" width="90%" alt="Detection Results">
</p>

📈 Analytics Dashboard

<p align="center">
  <img src="./Screenshots/analytics.PNG" width="90%" alt="Analytics Dashboard">
</p>

🎥 Processed Video

<p align="center">
  <img src="./Screenshots/process video.PNG" width="90%" alt="Processed Video">
</p>

🚀 How to Run Locally

1️⃣ Clone the Repository

git clone https://github.com/Tehmina124/AI-Object-Detection-Tracking.git

2️⃣ Open the Project Folder

cd AI-Object-Detection-Tracking

3️⃣ Create a Virtual Environment

python -m venv venv

4️⃣ Activate the Virtual Environment

Windows:

venv\Scripts\activate

5️⃣ Install Dependencies

python -m pip install -r requirements.txt

6️⃣ Run the Streamlit Application

python -m streamlit run app.py

7️⃣ Open in Browser

http://localhost:8501

📦 Required Dependencies

The project uses packages including:

streamlit
opencv-python
ultralytics
deep-sort-realtime
numpy
pandas

All required packages should be listed in:

requirements.txt

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment Flow

🐙 GitHub Repository
        ↓
📁 Upload Project Files
        ↓
📄 requirements.txt
        ↓
🎈 Connect Repository to Streamlit
        ↓
▶️ Deploy Application
        ↓
🌐 Public Live Demo

🎯 Project Objectives

The main objectives of this project are:

🤖 Implement object detection

🔍 Implement multi-object tracking

🆔 Assign unique IDs to detected objects

👤 Detect and track people

🚗 Detect and track vehicles

📍 Visualize object trajectories

🚨 Generate detection alerts

📊 Generate real-time statistics

📈 Generate final analytics

🎥 Process uploaded videos

⬇️ Allow users to download processed videos

🎈 Build an interactive Streamlit application

☁️ Deploy an AI application online

💡 What I Learned

Through this project, I gained practical experience in:

🐍 Python development

👁️ Computer Vision

🤖 YOLO object detection

🔍 DeepSORT object tracking

🎥 Video processing

📦 Bounding-box processing

🆔 Object identity tracking

📍 Trajectory visualization

🚨 Alert generation

📊 Data analytics

🎈 Streamlit development

🐙 Git & GitHub

☁️ Streamlit Cloud deployment

🔮 Future Improvements

Potential future improvements include:

🧠 Custom-trained YOLO models

🎯 Higher-accuracy detection

👥 Advanced crowd analysis

🚨 Real-time notification system

📧 Email alerts

📱 Mobile notifications

🔊 Audio alerts

📷 Live camera support

🌐 IP camera / CCTV integration

🧠 Advanced behavior detection

🚶 Person re-identification

🚗 License plate detection

📊 CSV/PDF analytics export

🗺️ Advanced tracking visualization

⚡ GPU-accelerated processing

🔐 User authentication

⭐ Project Highlights

Feature

Description

🤖 YOLO Detection

Detect objects in video frames

🔍 DeepSORT Tracking

Track objects across frames

🆔 Unique IDs

Maintain object identities

👤 People Detection

Detect and count people

🚗 Vehicle Detection

Detect multiple vehicle types

📍 Trajectories

Visualize object movement

🚨 Alerts

Generate detection alerts

📊 Live Statistics

Monitor processing in real time

📈 Analytics

Generate final statistics

📋 Tracking Report

Summarize tracking information

🎚️ Confidence Control

Adjust detection sensitivity

🎯 Object Filtering

Select object classes

🎥 Video Processing

Generate processed videos

⬇️ Download

Download processed results

☁️ Cloud Deployment

Public Streamlit application

🎓 Internship Project

DecodeLabs AI Internship — Task 4

👩‍💻 About Me

Tehmina Anwar

BSAI Student | AI/ML Engineer | Python Developer

I am a Bachelor of Science in Artificial Intelligence student interested in building practical applications using Artificial Intelligence, Machine Learning, Natural Language Processing, Generative AI, and Computer Vision.

🌟 Areas of Interest

🐍 Python

🤖 Machine Learning

🧠 Generative AI

💬 Large Language Models

🔎 Retrieval-Augmented Generation

📝 Natural Language Processing

👁️ Computer Vision

🚀 AI Application Development

🔗 Connect With Me

<p align="center">
  <a href="https://github.com/Tehmina124">💻 GitHub</a> •
  <a href="https://www.linkedin.com/in/tehmina-anwar-77b8a8414/">🔗 LinkedIn</a> •
  <a href="https://tehmina-portfolio-five.vercel.app/">🌐 Portfolio</a> •
  <a href="https://ai-object-detection-tracking-xoydqolhfxgcxmvefv45ac.streamlit.app/">🚀 Live Project</a>
</p>

⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ Star on GitHub.

Your support is greatly appreciated! ❤️

<p align="center">
  <b>🎯 Built with ❤️ using Python, YOLO, DeepSORT, OpenCV & Streamlit</b>
</p>

<p align="center">
  © 2026 <b>Tehmina Anwar</b> | DecodeLabs AI Internship | Task 4
</p>
