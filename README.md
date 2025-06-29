# Aeromano

*Air-powered hand gesture steering interface for hands-free gaming control.*

---

## 🚀 About the Project

**Aeromano** is an innovative hand-gesture-based virtual steering controller designed for controlling vehicles in PC games using only hand movements in front of your webcam. Built with OpenCV and MediaPipe, Aeromano translates your gestures into keyboard keystrokes, enabling immersive and contactless gaming experiences.

---

## 🧠 Features

* 🚗 **Steering**: Move your right hand left/right to steer (`A`/`D` keys)
* 🏎 **Acceleration/Braking**: Raise or lower your left hand to move forward (`W`) or brake/reverse (`S`)
* 👋 **Two-Hand Recognition**: Requires both hands in the frame to activate controls
* 🎮 **Game-Compatible**: Works with most PC games that use WASD controls

---

## 📸 Demo


[![Watch Demo](https://your-thumbnail-link.com)](https://your-demo-link.com)

---

## 🛠 Tech Stack

* [Python 3.10+](https://www.python.org/)
* [OpenCV](https://opencv.org/) – for camera input and visual feedback
* [MediaPipe](https://google.github.io/mediapipe/) – for real-time hand detection
* [pynput](https://pynput.readthedocs.io/) – for simulating continuous key presses

---

## 📁 Folder Structure

```
 
├── README.md
├── controls.py               # Main controller script
├── hand_tracking_module.py   # Hand detection class using MediaPipe
└── requirements.txt               
```

---

## 🧪 Usage

Run the controller:

```bash
python controls.py
```

**Exit gesture mode**: Press `j` key in the video window to quit.

---

## ✅ Requirements

* A webcam (built-in or USB)
* Basic lighting for better hand tracking
* Games that support `W`, `A`, `S`, `D` keys for control

---

## 📦 Dependencies (in `requirements.txt`)

```
opencv-python
mediapipe
pynput
```

---

## 🤝 Contributing

Feel free to fork this repo, open issues, or suggest features. Contributions are always welcome!

---

## 📬 Contact

**Author**: Shubham Jain
📧 Email: \[[shubh.j.0705@gmail.com](mailto:shubh.j.0705@gmail.com)]
🔗 LinkedIn: [Shubham Jain](https://www.linkedin.com/in/shubham--jain--/)

---

## 🏷 Tags

`gesture-control` `python` `mediapipe` `opencv` `hands-free` `virtual-controller` `aeromano`

---

**Give this repo a ⭐ if you liked it!**
