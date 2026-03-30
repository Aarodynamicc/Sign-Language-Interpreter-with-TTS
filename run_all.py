import os
import subprocess

print("🚀 Starting Sign Language Project Pipeline...\n")

# Step 1: Train model if not exists
model_path = "model/sign_model.h5"

if not os.path.exists(model_path):
    print("🧠 Training model...\n")
    subprocess.run(["python", "model/train_model.py"])
else:
    print("✅ Model already exists, skipping training.\n")

# Step 2: Check labels
labels_path = "model/labels.json"
if not os.path.exists(labels_path):
    print("⚠️ labels.json missing! Make sure training saves it.\n")

# Step 3: Run real-time inference
print("🎥 Starting real-time detection...\n")
subprocess.run(["python", "inference/realtime.py"])