# -------------------- IMPORT LIBRARIES --------------------
import cv2
import urllib.request
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# -------------------- MEDIAPIPE SETUP --------------------
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils


# -------------------- FUNCTION: LOAD IMAGE FROM URL --------------------
def url_to_array(url):
    try:
        req = urllib.request.urlopen(url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
    except Exception as e:
        print("Error loading image:", e)
        return None


# -------------------- IMAGE URL --------------------
mug_url = "https://t4.ftcdn.net/jpg/06/19/97/81/360_F_619978183_55XXYY6Szc8paQrDBG1UNZsRtCepVWD5.jpg"

image = url_to_array(mug_url)

if image is None:
    print("Failed to load image.")
    exit()


# -------------------- OBJECTRON MODEL --------------------
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name='Cup'  # Available: 'Shoe', 'Cup', 'Camera', 'Laptop'
) as objectron:

    results = objectron.process(image)

    if not results.detected_objects:
        print("No 3D objects detected.")
    else:
        print(f"Detected {len(results.detected_objects)} object(s).")

    annotated_image = image.copy()

    for detected_object in results.detected_objects:
        # Draw 2D bounding box landmarks
        mp_drawing.draw_landmarks(
            annotated_image,
            detected_object.landmarks_2d,
            mp_objectron.BOX_CONNECTIONS
        )

        # Draw 3D axis
        mp_drawing.draw_axis(
            annotated_image,
            detected_object.rotation,
            detected_object.translation
        )


# -------------------- DISPLAY RESULT --------------------
plt.figure(figsize=(10, 10))
plt.imshow(annotated_image)
plt.axis("off")
plt.title("3D Object Detection using MediaPipe Objectron")
plt.show()

# C:\Users\Admin\AppData\Local\Programs\Python\Python310\python.exe
