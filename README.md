# 🛡️ AI-Based Real-Time Monitoring for PPE Compliance
### AAE 4011: AI in Unmanned Autonomous Systems | Final Project

This repository contains a real-time safety monitoring system developed using **YOLOv11**. The system is designed to enhance industrial safety by automatically detecting Personal Protective Equipment (PPE) violations and sending instant alerts via Telegram.

---

## 🚀 Key Highlights
* **Deep Learning Model:** YOLOv11 (Nano) optimized over **100 training epochs**.
* **Performance:** Achieved an average inference speed of **323.4ms** per frame.
-   **Instant Alerting:** Integrated with **Telegram Bot API** for real-time violation notifications with photo evidence.
-   **Hardware Optimized:** Configured to run on **Apple Silicon (MPS)** and CPU environments.

---

## 📂 Repository Contents
| File | Description |
| :--- | :--- |
| 📄 `yolo11.py` | The main execution script for real-time detection & alerting. |
| 🧠 `best.pt` | **Custom-trained weights** (100 Epochs) for PPE detection. |
| 📋 `requirements.txt`| List of project dependencies (Ultralytics, OpenCV, Requests). |

---

## ⚙️ Core Functionality
The system monitors a live video feed and filters detections based on specific **Violation IDs** (e.g., *No_Helmet*, *No_Glove*). When a violation is identified:
1.  A visual frame is captured.
2.  The system calculates a confidence score.
3.  An automated message is sent to the safety supervisor's **Telegram** account.

---

## 📊 Evaluation Results
Based on our project validation (see Section 4 of the report):
- **Accuracy:** Successfully identified key safety gear in diverse lighting.
- **Speed:** Capable of real-time processing on standard laptop hardware.
- **Convergence:** Training loss successfully stabilized after 100 epochs, ensuring reliable detection.

---

## 🎥 Project Demonstration
Check out our system in action through these video clips:
- [📺 Demo Clip 1 - Real-Time Detection](https://youtu.be/u5vIJxIKNjs)
- [📺 Demo Clip 2 - Alert Verification](https://youtu.be/BhsmWFraiSY)
- [📺 Demo Clip 3 - System Integration](https://youtu.be/RoxD0rOsVew)

---

**Project Team:** 🎓 **Lee Hon Yan** (25025876D) & **Lee Tsz Nam** (25032937D)  
📅 **Submission Date:** 17/04/2026
