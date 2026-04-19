# 🛡️ AI-Based Real-Time Monitoring for PPE Compliance
### AAE 4011: AI in Unmanned Autonomous Systems | Final Project

This repository contains an automated safety monitoring system developed using **YOLOv11**. The project focuses on detecting Personal Protective Equipment (PPE) violations and bridging the gap between detection and action via automated alerts.

---

## 🚀 Key Highlights
* **Deep Learning Model:** YOLOv11 (Nano) optimized over **100 training epochs**.
* **Performance:** Achieved an average inference speed of **323.4ms** per frame.
* **Instant Alerting:** Integrated with **Telegram Bot API** to send violation evidence automatically.
* **Hardware Optimized:** Configured for **Apple Silicon (MPS)** and standard CPU environments.

---

## 📂 Repository Contents
| File | Description |
| :--- | :--- |
| 📄 `yolo11.py` | Main script for real-time video stream monitoring. |
| 📄 `predict.py` | **Static Image Analyzer:** Processes local images, detects violations, and sends Telegram alerts. |
| 🧠 `best.pt` | **Custom Weights:** The 5.5MB optimized model file from 100-epoch training. |
| 📋 `requirements.txt`| Project dependencies (Ultralytics, OpenCV, Requests). |

---

## ⚙️ Core Functionality (Static & Real-Time)
The system (especially `predict.py`) is programmed to identify specific **Violation IDs**:
- **ID 7 (No_Helmet):** Triggers a 🚨 "Missing Helmet" alert.
- **ID 5 (No_Glove):** Triggers a 🚨 "Missing Gloves" alert.

**Workflow of `predict.py`:**
1. **Analyze:** Scans a static image (e.g., from `test_data/`).
2. **Identify:** Detects if any safety gear is missing based on trained weights.
3. **Notify:** If a violation is found, it automatically uploads the annotated image to **Telegram** with a timestamped warning message.

---

## 📊 Evaluation Results
As documented in our project report:
- **Accuracy:** Reliable detection in diverse industrial lighting conditions.
- **Efficiency:** Small model footprint (5.5MB) allows for deployment on edge devices.
- **Validation:** Successfully verified via automated Telegram notifications.

---

## 🎥 Project Demonstration
- [📺 Demo Clip 1 - Detection](https://youtu.be/u5vIJxIKNjs)
- [📺 Demo Clip 2 - Detection](https://youtu.be/BhsmWFraiSY)
- [📺 Demo Clip 3 - Detection](https://youtu.be/RoxD0rOsVew)
- <img width="1920" height="1080" alt="violation_gloves" src="https://github.com/user-attachments/assets/bb8eb65c-26e8-44c7-89fd-b33daaaa9308" />
- <img width="971" height="754" alt="螢幕截圖 2026-04-19 下午7 18 16" src="https://github.com/user-attachments/assets/e8de4698-0e89-446c-a3b9-a0b9d6399ccd" />
-<img width="1048" height="799" alt="螢幕截圖 2026-04-12 下午4 45 19" src="https://github.com/user-attachments/assets/276fb4cb-546a-4d16-bb93-52b998a5df0d" />





---

**Project Team:** 🎓 **Lee Hon Yan** & **Lee Tsz Nam** Group 11 📅 **Submission Date:** 17/04/2026
