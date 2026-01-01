from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import cv2
import numpy as np
import os
import uuid
from gtts import gTTS

app = FastAPI(title="Perceva Object Detection API")

# ---------------- Models ---------------- #
custom_model = YOLO("model/best.pt")   # your trained model
pretrained_model = YOLO("yolov8n.pt")  # pretrained COCO model

# ---------------- Priority list ---------------- #
PRIORITY = ["car", "bus", "train", "motorcycle", "traffic light",
            "bicycle", "stop sign","truck", "person"]

# ---------------- Serve audio files ---------------- #
os.makedirs("audio", exist_ok=True)
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

# ---------------- Utility functions ---------------- #
def generate_sentence(objects):
    """Generate accessible text for detected objects."""
    if not objects:
        return "There is nothing around you."
    
    from collections import Counter
    counts = Counter(objects)
    phrases = []

    for obj, count in counts.items():
        if count == 1:
            phrases.append(f"a {obj}")
        else:
            phrases.append(f"{count} {obj}s")
    
    sentence = "there is " + " and ".join(phrases) + " nearby."
    return sentence

def sort_by_priority(detected):
    """Sort detected objects by priority list."""
    detected = list(set(detected))  # remove duplicates
    detected.sort(key=lambda x: PRIORITY.index(x) if x in PRIORITY else 999)
    return detected

def text_to_audio_file(text):
    """Generate TTS audio file and return file path."""
    filename = f"audio/tts_{uuid.uuid4()}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename

def detect_objects(img):
    """Detect objects using both custom and pretrained YOLO models."""
    results_custom = custom_model(img)[0]
    results_pretrained = pretrained_model(img)[0]

    detected_custom = [custom_model.names[int(box.cls)] for box in results_custom.boxes]
    detected_pretrained = [pretrained_model.names[int(box.cls)] for box in results_pretrained.boxes]

    detected = list(set(detected_custom + detected_pretrained))
    detected = sort_by_priority(detected)
    return detected

# ---------------- IMAGE ---------------- #
@app.post("/detect-image/")
async def detect_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    detected = detect_objects(img)
    sentence = generate_sentence(detected)
    audio_file = text_to_audio_file(sentence)

    return JSONResponse({
        "objects": detected,
        "sentence": sentence,
        "audio_url": f"/{audio_file}"
    })

# ---------------- VIDEO ---------------- #
@app.post("/detect-video/")
async def detect_video(file: UploadFile = File(...)):
    video_path = f"temp_{uuid.uuid4()}.mp4"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    cap = cv2.VideoCapture(video_path)
    detected_objects = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_detected = detect_objects(frame)
        detected_objects.extend(frame_detected)

    cap.release()
    os.remove(video_path)

    detected_objects = sort_by_priority(detected_objects)
    sentence = generate_sentence(detected_objects)
    audio_file = text_to_audio_file(sentence)

    return JSONResponse({
        "objects": detected_objects,
        "sentence": sentence,
        "audio_url": f"/{audio_file}"
    })

# ---------------- WEBCAM ---------------- #
@app.get("/detect-webcam/")
def detect_webcam(limit_frames: int = Query(50, ge=1, le=500)):
    cap = cv2.VideoCapture(0)
    detected_objects = []
    frame_count = 0

    while cap.isOpened() and frame_count < limit_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame_detected = detect_objects(frame)
        detected_objects.extend(frame_detected)
        frame_count += 1

    cap.release()

    detected_objects = sort_by_priority(detected_objects)
    sentence = generate_sentence(detected_objects)
    audio_file = text_to_audio_file(sentence)

    return JSONResponse({
        "objects": detected_objects,
        "sentence": sentence,
        "audio_url": f"/{audio_file}"
    })
