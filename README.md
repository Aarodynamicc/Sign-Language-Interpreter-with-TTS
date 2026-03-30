# 🤟 Sign Language Recognition System

## 📌 Project Overview

This project aims to build a **real-time sign language recognition system** using deep learning.
The system captures hand gestures via webcam, processes them using a trained model, and converts the recognized signs into **text and speech output**.

---

## 🚀 Features (Planned / In Progress)

* Real-time hand detection using **MediaPipe**
* Gesture classification using a deep learning model (**EfficientNet-based CNN**)
* Text output of predicted sign
* Speech output using Text-to-Speech (TTS)
* Modular project structure for scalability

---

## ⚠️ Important Notice

> 🚧 **This project is currently under development.**

* The **model training and inference pipeline are not fully implemented yet**
* Code structure is prepared, but execution may not be complete or stable
* Further development and debugging are required

---

## 📂 Dataset Information

⚠️ **Dataset is NOT included in this repository**

Due to size constraints, the dataset used for training is not provided here.

### 📥 Dataset Used

* ASL Alphabet Dataset from Kaggle
* Link: https://www.kaggle.com/grassknoted/asl-alphabet

### 📊 Dataset Details

* Contains images for:

  * Alphabets (A–Z)
  * Additional classes (space, delete, nothing — optional)
* Approximately 1000+ images per class

---

## 📁 Expected Dataset Structure

After downloading and organizing:

```
data/
  train/
    A/
    B/
    ...
  val/
    A/
    B/
    ...
```

* Each folder represents one class label
* Images must be placed inside corresponding folders
* A train/validation split is required

---

## 🧠 Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* MediaPipe
* NumPy
* gTTS (Text-to-Speech)

---

## 🛠️ Current Project Structure

```
sign_language_project/
│
├── data/                 # Dataset (not included)
├── model/                # Training scripts and model files
├── inference/            # Real-time prediction code
├── utils/                # Helper modules (preprocessing, tracking, speech)
├── run_all.py            # Automation script
└── requirements.txt      # Dependencies
```

---

## ▶️ How to Run (Once Implemented)

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Train the model:

   ```
   python model/train_model.py
   ```

3. Run real-time detection:

   ```
   python inference/realtime.py
   ```

---

## 🧪 Current Status

| Module              | Status         |
| ------------------- | -------------- |
| Dataset Setup       | ✅ Done         |
| Project Structure   | ✅ Done         |
| Model Training      | 🚧 In Progress |
| Real-time Inference | 🚧 In Progress |
| Speech Output       | 🚧 In Progress |

---

## 📌 Notes

* Dataset must be downloaded manually from Kaggle
* GPU acceleration setup is not included in this repository
* Performance depends on dataset quality and training setup

---

## 🧾 Future Improvements

* Improve model accuracy with data augmentation
* Add GUI interface
* Support word/sentence formation
* Optimize real-time performance
* Deploy as a web or mobile application

---

## 📜 License

This project is for educational purposes.

---

## 🙌 Acknowledgements

* Kaggle for dataset
* Open-source libraries used in this project

---

🔥 *Project is under active development. Stay tuned for updates.*
