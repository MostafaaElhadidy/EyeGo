# 🎯 OpenCV Real-Time Object Tracker

A lightweight Python application that performs **real-time object tracking** using
OpenCV's CSRT (Channel and Spatial Reliability Tracking) algorithm and your webcam.

## 🧠 Implementation Details

### Algorithm: CSRT

This project uses **CSRT (Discriminative Correlation Filter with Channel and Spatial
Reliability)**. It was chosen over the faster MOSSE algorithm because:

- It handles **partial occlusion** better (object briefly hidden)
- It adapts to **scale changes** (object getting closer/further)
- It maintains tracking through **rotation and deformation**
- Accuracy trades off slightly against MOSSE's raw speed, which is acceptable
  for most webcam frame rates (25–60 FPS)

### How It Works

1. **ROI Selection** — On launch, the first frame is frozen and the user draws a
   bounding box around the target object using `cv2.selectROI`.
2. **Tracker Initialization** — The CSRT tracker learns the pixel pattern inside
   the selected box as its reference template.
3. **Frame-by-Frame Update** — Each new webcam frame is fed to `tracker.update()`,
   which returns a new `(x, y, w, h)` bounding box representing the object's
   predicted new location.
4. **Visual Overlay** — A blue rectangle is drawn around the tracked object, along
   with a green "Now Tracking" label and a red FPS counter.
5. **Loss Detection** — If `tracker.update()` returns `success=False`, a red
   "Lost tracking" warning is displayed.

### FPS Calculation

```
fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
```

`getTickCount()` snapshots the CPU clock at the start and end of each frame.
Dividing the CPU frequency by the elapsed ticks gives real-time FPS.

## ⚙️ Requirements

- Python 3.8+
- Webcam (built-in or USB)
- OpenCV contrib (for legacy tracker access)

## 🚀 Deployment / Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MostafaaElhadidy/EyeGo.git
cd EyeGo
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-contrib-python
```

> ⚠️ You must install `opencv-contrib-python` (not just `opencv-python`) to
> access `cv2.legacy` trackers like CSRT and MOSSE.

### 4. Run the Tracker

```bash
python EyeGo Project.py
```

---

## 🕹️ How to Use

1. Run the script — your webcam feed opens in a window
2. **Draw a box** around the object you want to track by clicking and dragging
3. Press **Enter** or **Space** to confirm the selection
4. The tracker starts — a **blue box** follows your object in real time
5. Press **`q`** at any time to quit

## 📦 requirements.txt

```
opencv-contrib-python>=4.5.0
```
