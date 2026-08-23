import streamlit as st
import cv2
import tempfile
import os
import time
from collections import Counter, defaultdict

from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Object Detection & Tracking",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 5px;
    }

    .author {
        text-align: center;
        font-size: 16px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎯 AI Object Detection & Tracking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'YOLO + DeepSORT based intelligent object detection, tracking and analytics'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="author">'
    '👩‍💻 Developed by <b>Tehmina Anwar</b> | '
    'Decode Labs Internship — Task 4'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# LOAD YOLO MODEL
# =========================================================

@st.cache_resource
def load_yolo_model():

    model = YOLO("yolov8n.pt")

    return model


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("⚙️ Detection Settings")


confidence_threshold = st.sidebar.slider(
    "🎚️ Confidence Threshold",
    min_value=0.10,
    max_value=0.95,
    value=0.50,
    step=0.05
)


display_every = st.sidebar.slider(
    "🖼️ Preview Every N Frames",
    min_value=1,
    max_value=30,
    value=10,
    step=1
)


st.sidebar.markdown("---")


# =========================================================
# OBJECT FILTER
# =========================================================

st.sidebar.subheader("🎯 Object Filter")


available_classes = [
    "person",
    "car",
    "bus",
    "truck",
    "motorcycle",
    "bicycle",
    "dog",
    "cat",
    "bird"
]


selected_classes = st.sidebar.multiselect(
    "Select objects to track",
    available_classes,
    default=[
        "person",
        "car",
        "bus",
        "truck",
        "motorcycle",
        "bicycle"
    ]
)


st.sidebar.markdown("---")


# =========================================================
# TRACKING PATH
# =========================================================

st.sidebar.subheader("📍 Tracking Path")


show_trajectories = st.sidebar.checkbox(
    "Show Object Trajectories",
    value=True
)


trajectory_length = st.sidebar.slider(
    "Trajectory Length",
    min_value=5,
    max_value=100,
    value=30,
    step=5
)


st.sidebar.markdown("---")


# =========================================================
# ALERT SETTINGS
# =========================================================

st.sidebar.subheader("🚨 Alert Settings")


person_alert_limit = st.sidebar.slider(
    "👤 Person Alert Limit",
    min_value=1,
    max_value=20,
    value=3
)


object_alert_limit = st.sidebar.slider(
    "🎯 Object Limit",
    min_value=1,
    max_value=20,
    value=8
)


vehicle_alert_enabled = st.sidebar.checkbox(
    "🚗 Enable Vehicle Alerts",
    value=True
)


st.sidebar.markdown("---")


st.sidebar.info(
    "💡 Higher confidence means fewer but more reliable detections."
)


# =========================================================
# VIDEO UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📁 Upload a Video",
    type=[
        "mp4",
        "avi",
        "mov",
        "mkv"
    ]
)


# =========================================================
# WELCOME SCREEN
# =========================================================

if uploaded_file is None:

    st.info(
        "👆 Upload an MP4, AVI, MOV or MKV video "
        "to start object detection and tracking."
    )

    st.markdown(
        """
        ## 🚀 Project Features

        - 🎯 YOLO Object Detection
        - 🆔 DeepSORT Object Tracking
        - 👤 People Detection
        - 🚗 Vehicle Detection
        - 🆔 Unique Object IDs
        - 📍 Object Tracking Trajectories
        - 📊 Live Statistics
        - 📈 Advanced Analytics
        - 🚨 Live Alerts
        - 📋 Alert History
        - 📊 Detection Charts
        - 🎚️ Confidence Control
        - 🎯 Object Class Filtering
        - 🎥 Processed Video
        - ⬇️ Download Processed Video

        ### 🛠️ Technologies

        **Python • Streamlit • OpenCV • YOLO • DeepSORT**

        👩‍💻 Developed by **Tehmina Anwar**

        🏢 Decode Labs Internship — **Task 4**
        """
    )

    st.stop()


# =========================================================
# SAVE UPLOADED VIDEO
# =========================================================

suffix = os.path.splitext(
    uploaded_file.name
)[1]

if suffix.lower() not in [
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
]:
    suffix = ".mp4"


input_file = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=suffix
)

input_file.write(
    uploaded_file.getbuffer()
)

input_file.close()

input_path = input_file.name


# =========================================================
# ORIGINAL VIDEO
# =========================================================

st.subheader("🎥 Original Video")

st.video(
    uploaded_file
)


# =========================================================
# START BUTTON
# =========================================================

start_detection = st.button(
    "🚀 Start Detection & Tracking",
    type="primary",
    use_container_width=True
)


if not start_detection:

    st.info(
        "👆 Click **Start Detection & Tracking** "
        "to begin processing."
    )

    st.stop()


# =========================================================
# LOAD MODEL
# =========================================================

try:

    with st.spinner(
        "🤖 Loading YOLO model..."
    ):

        model = load_yolo_model()

except Exception as e:

    st.error(
        f"❌ Could not load YOLO model: {e}"
    )

    try:
        os.remove(input_path)
    except Exception:
        pass

    st.stop()


# =========================================================
# DEEPSORT
# =========================================================

try:

    tracker = DeepSort(
        max_age=30,
        n_init=3
    )

except Exception as e:

    st.error(
        f"❌ Could not initialize DeepSORT: {e}"
    )

    try:
        os.remove(input_path)
    except Exception:
        pass

    st.stop()


# =========================================================
# OPEN VIDEO
# =========================================================

cap = cv2.VideoCapture(
    input_path
)


if not cap.isOpened():

    st.error(
        "❌ Could not open the uploaded video."
    )

    try:
        os.remove(input_path)
    except Exception:
        pass

    st.stop()


# =========================================================
# VIDEO INFORMATION
# =========================================================

fps = cap.get(
    cv2.CAP_PROP_FPS
)

if fps <= 0:
    fps = 25


frame_width = int(
    cap.get(
        cv2.CAP_PROP_FRAME_WIDTH
    )
)


frame_height = int(
    cap.get(
        cv2.CAP_PROP_FRAME_HEIGHT
    )
)


total_frames = int(
    cap.get(
        cv2.CAP_PROP_FRAME_COUNT
    )
)


duration = (
    total_frames / fps
    if fps > 0
    else 0
)


# =========================================================
# VIDEO INFO
# =========================================================

st.subheader(
    "📹 Video Information"
)


info1, info2, info3, info4 = st.columns(4)


info1.metric(
    "Resolution",
    f"{frame_width} × {frame_height}"
)


info2.metric(
    "Video FPS",
    f"{fps:.1f}"
)


info3.metric(
    "Total Frames",
    total_frames
)


info4.metric(
    "Duration",
    f"{duration:.1f} sec"
)


# =========================================================
# OUTPUT VIDEO
# =========================================================

output_file = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".mp4"
)

output_path = output_file.name

output_file.close()


# =========================================================
# VIDEO WRITER
# =========================================================

fourcc = cv2.VideoWriter_fourcc(
    *"mp4v"
)


out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (
        frame_width,
        frame_height
    )
)


if not out.isOpened():

    cap.release()

    st.error(
        "❌ Could not create output video."
    )

    try:
        os.remove(input_path)
    except Exception:
        pass

    st.stop()


# =========================================================
# PROCESSING UI
# =========================================================

st.subheader(
    "⏳ Processing"
)


progress_bar = st.progress(
    0
)


status_text = st.empty()


frame_display = st.empty()


# =========================================================
# LIVE STATISTICS
# =========================================================

st.subheader(
    "📊 Live Statistics"
)


stat1, stat2, stat3, stat4 = st.columns(4)


total_objects_placeholder = stat1.empty()

people_placeholder = stat2.empty()

vehicles_placeholder = stat3.empty()

processing_fps_placeholder = stat4.empty()


# =========================================================
# LIVE ALERTS
# =========================================================

st.subheader(
    "🚨 Live Alerts"
)


live_alert_placeholder = st.empty()


# =========================================================
# VARIABLES
# =========================================================

frame_number = 0

unique_track_ids = set()

unique_people_ids = set()

unique_vehicle_ids = set()

detection_counter = Counter()

unique_class_ids = defaultdict(set)

trajectories = defaultdict(list)

max_objects_in_frame = 0

total_detection_events = 0

start_time = time.time()

processing_fps = 0


# =========================================================
# ALERT VARIABLES
# =========================================================

person_alert_count = 0

vehicle_alert_count = 0

limit_alert_count = 0

alert_log = []

previous_person_alert = False

previous_vehicle_alert = False

previous_limit_alert = False


# =========================================================
# CLASS NAMES
# =========================================================

class_names = model.names


# =========================================================
# VEHICLE CLASSES
# =========================================================

vehicle_classes = {
    "car",
    "bus",
    "truck",
    "motorcycle",
    "bicycle"
}


# =========================================================
# FRAME LOOP
# =========================================================

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1


    # =====================================================
    # YOLO
    # =====================================================

    try:

        results = model(
            frame,
            verbose=False
        )

    except Exception as e:

        st.error(
            f"❌ YOLO detection error: {e}"
        )

        break


    detections = []


    # =====================================================
    # EXTRACT DETECTIONS
    # =====================================================

    for result in results:

        for box in result.boxes:

            confidence = float(
                box.conf[0]
            )

            class_id = int(
                box.cls[0]
            )


            if confidence < confidence_threshold:
                continue


            try:

                class_name = class_names[
                    class_id
                ]

            except Exception:

                class_name = "Object"


            if (
                selected_classes
                and class_name not in selected_classes
            ):
                continue


            x1, y1, x2, y2 = (
                box.xyxy[0].tolist()
            )


            width = x2 - x1

            height = y2 - y1


            detections.append(
                (
                    [
                        x1,
                        y1,
                        width,
                        height
                    ],
                    confidence,
                    class_id
                )
            )


    # =====================================================
    # DEEPSORT
    # =====================================================

    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )


    # =====================================================
    # CURRENT COUNTERS
    # =====================================================

    current_objects = 0

    current_people = 0

    current_vehicles = 0


    # =====================================================
    # DRAW TRACKS
    # =====================================================

    for track in tracks:

        if not track.is_confirmed():
            continue


        track_id = track.track_id


        x1, y1, x2, y2 = map(
            int,
            track.to_ltrb()
        )


        x1 = max(
            0,
            x1
        )

        y1 = max(
            0,
            y1
        )

        x2 = min(
            frame_width,
            x2
        )

        y2 = min(
            frame_height,
            y2
        )


        if x2 <= x1 or y2 <= y1:
            continue


        unique_track_ids.add(
            track_id
        )


        current_objects += 1


        max_objects_in_frame = max(
            max_objects_in_frame,
            current_objects
        )


        # =================================================
        # CLASS
        # =================================================

        class_name = "Object"


        try:

            if track.det_class is not None:

                class_name = class_names[
                    int(track.det_class)
                ]

        except Exception:

            class_name = "Object"


        # =================================================
        # PEOPLE
        # =================================================

        if class_name == "person":

            current_people += 1

            unique_people_ids.add(
                track_id
            )


        # =================================================
        # VEHICLES
        # =================================================

        if class_name in vehicle_classes:

            current_vehicles += 1

            unique_vehicle_ids.add(
                track_id
            )


        # =================================================
        # UNIQUE CLASS IDs
        # =================================================

        unique_class_ids[
            class_name
        ].add(
            track_id
        )


        # =================================================
        # DETECTION COUNTER
        # =================================================

        detection_counter[
            class_name
        ] += 1


        total_detection_events += 1


        # =================================================
        # TRAJECTORY
        # =================================================

        center_x = int(
            (x1 + x2) / 2
        )

        center_y = int(
            (y1 + y2) / 2
        )


        trajectories[
            track_id
        ].append(
            (
                center_x,
                center_y
            )
        )


        if len(
            trajectories[track_id]
        ) > trajectory_length:

            trajectories[
                track_id
            ] = trajectories[
                track_id
            ][-trajectory_length:]


        # =================================================
        # BOX COLOR
        # =================================================

        if class_name == "person":

            box_color = (
                0,
                255,
                0
            )

        elif class_name in vehicle_classes:

            box_color = (
                255,
                150,
                0
            )

        else:

            box_color = (
                255,
                0,
                255
            )


        # =================================================
        # TRAJECTORY
        # =================================================

        if show_trajectories:

            points = trajectories[
                track_id
            ]


            for i in range(
                1,
                len(points)
            ):

                cv2.line(
                    frame,
                    points[i - 1],
                    points[i],
                    box_color,
                    2
                )


        # =================================================
        # BOX
        # =================================================

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            box_color,
            2
        )


        # =================================================
        # LABEL
        # =================================================

        label = (
            f"{class_name} "
            f"ID:{track_id}"
        )


        cv2.putText(
            frame,
            label,
            (
                x1,
                max(y1 - 10, 20)
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2
        )


# =========================================================
# ALERT CONDITIONS
# =========================================================

    current_alerts = []


    # =====================================================
    # PERSON ALERT
    # =====================================================

    person_alert = (
        current_people >= person_alert_limit
    )


    if person_alert:

        current_alerts.append(
            f"👤 High people count: {current_people}"
        )


        if not previous_person_alert:

            person_alert_count += 1

            alert_log.append(
                {
                    "Frame": frame_number,
                    "Type": "Person Alert",
                    "Message":
                        f"{current_people} people detected"
                }
            )


    previous_person_alert = person_alert


    # =====================================================
    # VEHICLE ALERT
    # =====================================================

    vehicle_alert = (
        vehicle_alert_enabled
        and current_vehicles > 0
    )


    if vehicle_alert:

        current_alerts.append(
            f"🚗 Vehicle detected: {current_vehicles}"
        )


        if not previous_vehicle_alert:

            vehicle_alert_count += 1

            alert_log.append(
                {
                    "Frame": frame_number,
                    "Type": "Vehicle Alert",
                    "Message":
                        f"{current_vehicles} vehicles detected"
                }
            )


    previous_vehicle_alert = vehicle_alert


    # =====================================================
    # OBJECT LIMIT ALERT
    # =====================================================

    limit_alert = (
        current_objects >= object_alert_limit
    )


    if limit_alert:

        current_alerts.append(
            f"⚠️ Object limit reached: {current_objects}"
        )


        if not previous_limit_alert:

            limit_alert_count += 1

            alert_log.append(
                {
                    "Frame": frame_number,
                    "Type": "Limit Alert",
                    "Message":
                        f"{current_objects} objects detected"
                }
            )


    previous_limit_alert = limit_alert


    # =====================================================
    # LIVE ALERT DISPLAY
    # =====================================================

    if current_alerts:

        alert_text = "\n\n".join(
            current_alerts
        )

        live_alert_placeholder.warning(
            "🚨 ACTIVE ALERTS\n\n"
            + alert_text
        )

    else:

        live_alert_placeholder.success(
            "🟢 No active alerts in current frame"
        )


    # =====================================================
    # PROCESSING FPS
    # =====================================================

    elapsed = (
        time.time()
        - start_time
    )


    if elapsed > 0:

        processing_fps = (
            frame_number
            / elapsed
        )


    # =====================================================
    # SAVE FRAME
    # =====================================================

    out.write(
        frame
    )


    # =====================================================
    # PROGRESS
    # =====================================================

    if total_frames > 0:

        progress = (
            frame_number
            / total_frames
        )


        progress_bar.progress(
            min(
                progress,
                1.0
            )
        )


    # =====================================================
    # STATUS
    # =====================================================

    status_text.write(
        f"Processing frame "
        f"{frame_number} / "
        f"{total_frames}"
    )


    # =====================================================
    # LIVE METRICS
    # =====================================================

    total_objects_placeholder.metric(
        "🎯 Current Objects",
        current_objects
    )


    people_placeholder.metric(
        "👤 People",
        current_people
    )


    vehicles_placeholder.metric(
        "🚗 Vehicles",
        current_vehicles
    )


    processing_fps_placeholder.metric(
        "⚡ Processing FPS",
        f"{processing_fps:.1f}"
    )


    # =====================================================
    # PREVIEW
    # =====================================================

    if (
        frame_number % display_every == 0
        or frame_number == 1
    ):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        frame_display.image(
            rgb_frame,
            channels="RGB",
            use_container_width=True
        )


# =========================================================
# RELEASE VIDEO
# =========================================================

cap.release()

out.release()


progress_bar.progress(
    1.0
)


processing_time = (
    time.time()
    - start_time
)


status_text.success(
    "✅ Detection and tracking completed!"
)


# =========================================================
# FINAL ANALYTICS
# =========================================================

st.subheader(
    "📈 Final Analytics"
)


final1, final2, final3, final4 = st.columns(4)


final1.metric(
    "🆔 Unique Objects",
    len(unique_track_ids)
)


final2.metric(
    "👤 Unique People",
    len(unique_people_ids)
)


final3.metric(
    "🚗 Unique Vehicles",
    len(unique_vehicle_ids)
)


final4.metric(
    "⏱️ Processing Time",
    f"{processing_time:.1f} sec"
)


# =========================================================
# ADVANCED ANALYTICS
# =========================================================

st.subheader(
    "📊 Advanced Analytics"
)


extra1, extra2, extra3 = st.columns(3)


extra1.metric(
    "🎯 Max Objects / Frame",
    max_objects_in_frame
)


extra2.metric(
    "🔢 Detection Events",
    total_detection_events
)


extra3.metric(
    "⚡ Average Processing FPS",
    f"{processing_fps:.2f}"
)


# =========================================================
# ALERT SUMMARY
# =========================================================

st.subheader(
    "🚨 Alert Summary"
)


alert1, alert2, alert3, alert4 = st.columns(4)


alert1.metric(
    "👤 Person Alerts",
    person_alert_count
)


alert2.metric(
    "🚗 Vehicle Alerts",
    vehicle_alert_count
)


alert3.metric(
    "⚠️ Limit Alerts",
    limit_alert_count
)


alert4.metric(
    "🔔 Total Alerts",
    len(alert_log)
)


# =========================================================
# ALERT HISTORY
# =========================================================

st.subheader(
    "📋 Detection Alert Log"
)


if alert_log:

    st.dataframe(
        alert_log,
        use_container_width=True,
        hide_index=True
    )

else:

    st.success(
        "🟢 No alerts were triggered during this video."
    )


# =========================================================
# TRACKING PATH SUMMARY
# =========================================================

st.subheader(
    "📍 Tracking Path Summary"
)


path_summary = []


for track_id, points in trajectories.items():

    if points:

        path_summary.append(
            {
                "Track ID": track_id,
                "Path Points": len(points),
                "Start Position":
                    str(points[0]),
                "Last Position":
                    str(points[-1])
            }
        )


if path_summary:

    st.dataframe(
        path_summary,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No tracking paths available."
    )


# =========================================================
# UNIQUE OBJECT SUMMARY
# =========================================================

st.subheader(
    "🆔 Unique Object Summary"
)


unique_summary = []


for object_name, ids in sorted(
    unique_class_ids.items()
):

    unique_summary.append(
        {
            "Object": object_name,
            "Unique IDs": len(ids)
        }
    )


if unique_summary:

    st.dataframe(
        unique_summary,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# DETECTION COUNTS
# =========================================================

st.subheader(
    "📊 Object Detection Counts"
)


if detection_counter:

    chart_data = {
        "Object": [],
        "Count": []
    }


    for object_name, count in (
        detection_counter.most_common()
    ):

        chart_data[
            "Object"
        ].append(
            object_name
        )


        chart_data[
            "Count"
        ].append(
            count
        )


    st.dataframe(
        chart_data,
        use_container_width=True,
        hide_index=True
    )


    st.subheader(
        "📊 Detection Chart"
    )


    st.bar_chart(
        chart_data,
        x="Object",
        y="Count"
    )

else:

    st.warning(
        "⚠️ No objects were detected."
    )


# =========================================================
# PROCESSED VIDEO
# =========================================================

st.subheader(
    "🎯 Processed Video"
)


try:

    with open(
        output_path,
        "rb"
    ) as video:

        video_bytes = video.read()


    st.video(
        video_bytes
    )


    st.download_button(
        label="⬇️ Download Processed Video",
        data=video_bytes,
        file_name="object_tracking_output.mp4",
        mime="video/mp4",
        type="primary",
        use_container_width=True
    )


except Exception as e:

    st.error(
        f"❌ Could not load processed video: {e}"
    )


# =========================================================
# FINAL SUCCESS
# =========================================================

st.success(
    "🎉 Task 4 completed successfully! "
    "AI Object Detection & Tracking analysis is ready."
)


# =========================================================
# CLEANUP
# =========================================================

try:

    os.remove(
        input_path
    )

except Exception:

    pass
