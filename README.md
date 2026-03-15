# SR2-GBG Robotics Controller

This repository contains the autonomous control logic for a competition robot built on the **Student Robotics (SR)** platform. It utilizes a combination of computer vision (OpenCV) and marker tracking to navigate, identify "gold" objects, and interact with markers.

---

## 🤖 Core Functionality

* **Autonomous Navigation:** Implements `drv`, `turn`, and `omni` movement functions using dual motor boards (`SR0TBG` and `SR0GJ1B`).
* **Computer Vision (OpenCV):**
    * **Color Filtering:** Uses HSV thresholding to identify "gold" objects in the environment.
    * **Contour Detection:** Uses Canny edge detection and contour sorting to find and center the robot on the largest detected gold object.
* **Marker Tracking:** Leverages the `R.camera.see()` API to identify specific cubes (ID 73) and wall markers for arena localization.
* **Claw Control:** Manages a servo-driven claw assembly (Servo 10) for grabbing and moving game elements.

---

## 🛠 Hardware Configuration

| Component | Port/ID | Description |
| :--- | :--- | :--- |
| **Servo** | Index 10 | Claw open/close mechanism |
| **Motor Board 1** | `SR0TBG` | Drive Motors (Wheels) |
| **Motor Board 2** | `SR0GJ1B` | Claw/Vertical movement motors |
| **Camera** | Built-in | Used for OpenCV processing and Marker ID tracking |

---

## 📂 Key Software Modules

### 1. Vision Processing
* `Filter()`: Captures an image and applies a gold HSV mask.
* `box()`: Analyzes the mask using `findContours` to return the coordinates of the largest gold item.

### 2. Navigation Logic
* `drvToMarker1/2/3()`: Different logic iterations for approaching cubes. These functions include logic to:
    * Search for cubes by turning if none are visible.
    * Calculate distance and offset from center.
    * Adjust motor power proportionally to steer toward the target.

### 3. Safety & Utilities
* `safeCheck()`: Scans the camera feed to ensure the path is clear of specific markers within a certain coordinate range.
* `isItCube()` / `isItWall()`: Filter functions to distinguish between game tokens and arena boundaries.

---

## 🚀 Execution Flow
1. **Initialize:** Robot starts, sets the servo to an open position, and waits for the official start signal.
2. **Search:** The robot drives forward and utilizes the `box()` function to locate gold via OpenCV.
3. **Align & Collect:** Uses marker-based tracking to refine its approach and secure the target.
4. **Obstacle Avoidance:** Continuously checks for wall markers to ensure it stays within the field of play.
