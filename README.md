# 🛠️ Hardware Tools Detection Web App using YOLO and Streamlit

This project is a computer vision web application that identifies common hardware tools like **hammers** and **spanners** from uploaded images. Built using **YOLOv5**, the app allows users to upload images and receive real-time object detection results. The web interface is powered by **Streamlit** and is fully responsive on desktop and mobile browsers.

---

## 🚀 Live Demo

👉 [Click here to run the app on Streamlit Cloud](https://hardware-tool-kit.streamlit.app/)

---

## 📦 Tech Stack

| Component           | Technology                                      |
| ------------------- | ----------------------------------------------- |
| 🧠 Model            | YOLOv5 → ONNX                                   |
| 📦 Deployment       | Streamlit Cloud                                 |
| 🐍 Backend          | Python                                          |
| 🖼 Annotation       | LabelImg                                        |
| 📷 Image Processing | OpenCV, Pillow                                  |
| 📁 Dependencies     | `opencv-python`, `numpy`, `pyyaml`, `streamlit` |

---

## 📸 Dataset Preparation

* I collected real-world images of **hardware tools** such as hammers and spanners from  the web.
* Used **LabelImg** to annotate images and generate YOLO-format labels.
* Each image was annotated with bounding boxes identifying object locations.

> ✅ Tip: Save labels in YOLO format and ensure class names are correctly listed in `data.yaml`.

---

## 🧠 Model Training (YOLOv5)

* Used Ultralytics' [YOLOv5 GitHub repo](https://github.com/ultralytics/yolov5)


> **Note**: Due to limited training time, this model currently detects only **two objects**: hammers and spanners.

---

## 🌐 Web App Features

* Upload JPEG or PNG hardware images
* View image metadata (size, type)
* Preview uploaded images
* Run YOLO detection and show result with bounding boxes
* Works on mobile and desktop browsers
* Add to Android home screen like a native app

---

## 🧹 Streamlit App Structure

```text
hardware-object-detection/
│
├── images/
│   ├── home.png
│   └── object.png
│
├── pages/
│   └── 1_yolo_for_image.py
│
├── yolo_predictions_1.py
├── data.yaml
├── best.onnx
├── requirements.txt
└── Home.py
```

---

## ⚠️ Challenges Faced

1. **Annotation Quality**
   Annotating large datasets manually using LabelImg was time-consuming and required careful attention to avoid mislabeling.

2. **Class Imbalance**
   Certain tools had fewer training examples, requiring image augmentation to balance the dataset.

3. **Hardware Limitations**
   Training was done on a consumer GPU (e.g., RTX 3050), so model size and epochs had to be optimized for faster training.

4. **ONNX Conversion Bugs**
   Needed to fix input shape mismatches when converting from `.pt` to `.onnx`.

5. **Streamlit CV Limitations**
   Webcam or video stream is not directly supported in Streamlit for mobile — only image uploads.

6. **Limited Time for Training**
   The model was trained for a short period, allowing classification of only **two hardware objects**.

---

## 📲 Mobile Access

* The deployed Streamlit app works on Android phones and browsers.
* To simulate a mobile app:

  * Open the link in Chrome on Android.
  * Tap `⋮` → **Add to Home screen**

---

## 📃 License

This project is for educational and personal demonstration purposes. Attribution is appreciated.

---

## 🙌 Author

Shehan
