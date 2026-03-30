import cv2
import numpy as np
from collections import deque, Counter
from tensorflow.keras.models import load_model

from utils.hand_tracker import HandTracker
from utils.preprocess import preprocess_image
from utils.speech import speak
import json

with open("../model/labels.json") as f:
    class_indices = json.load(f)

labels = list(class_indices.keys())
# Load model
model = load_model("../model/sign_model.h5")

# Load class labels
classes = list(model.output_shape)
# Replace this with actual class labels manually if needed
labels = [
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
] # <-- EDIT THIS

tracker = HandTracker()

cap = cv2.VideoCapture(0)

pred_queue = deque(maxlen=10)
last_spoken = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    bbox = tracker.get_hand_bbox(frame)

    if bbox:
        x1, y1, x2, y2 = bbox
        hand = frame[y1:y2, x1:x2]

        if hand.size != 0:
            img = preprocess_image(hand)
            pred = model.predict(img, verbose=0)
            class_id = np.argmax(pred)
            label = labels[class_id]

            pred_queue.append(label)

            # Stabilization
            if len(pred_queue) == 10:
                most_common = Counter(pred_queue).most_common(1)[0][0]

                if most_common != last_spoken:
                    speak(most_common)
                    last_spoken = most_common

            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("Sign Language Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()