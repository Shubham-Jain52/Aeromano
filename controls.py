import cv2 as cv
import mediapipe as mp
from hand_tracking_module import hand_detection
import keyboard as ky

present_key=[]

def hold_key(key):
    if key not in present_key:
        ky.press(key)
        present_key.append(key)

def rels_key(key):
    for p in key:
        if p in present_key:
            ky.release(p)
            present_key.remove(p)


vid = cv.VideoCapture(0)
detector = hand_detection()

# Frame counters and held key
left_frames = 0
right_frames = 0
forward_frames = 0
backward_frames = 0
hold_threshold = 5
current_key_down = None

while True:
    isTrue, frame = vid.read()
    if not isTrue:
        break
    frame = cv.flip(frame, 1)
    height, width = frame.shape[:2]
    center = (width // 2, height // 2)

    cv.circle(frame, center, radius=200, color=(0, 0, 225), thickness=3)
    cv.line(frame, (320, 40), (320, 440), (0, 225, 0), 5)
    cv.line(frame, (120, 240), (520, 240), (225, 0, 0), 5)

    image = detector.detection(frame)
    landmarks = detector.find_position(frame)

    pos = []
    for hands in landmarks:
        lm = hands['landmarks']
        x_coords = [i[1] for i in lm]
        y_coords = [i[2] for i in lm]

        if x_coords and y_coords:
            x_avg = int(sum(x_coords) / len(x_coords))
            y_avg = int(sum(y_coords) / len(y_coords))
            pos.append(
                {
                    "hand": "left" if hands['index'] == 0 else "right",
                    "x_coord": x_avg,
                    "y_coord": y_avg
                }
            )

    left_hand = next((p for p in pos if p['hand'] == "left"), None)
    right_hand = next((p for p in pos if p['hand'] == "right"), None)

    steer_threshold = (width * 3) // 4
    acc_threshold = height // 2
    buffer = 100

    print(f"left {left_hand}, right {right_hand}")

    
    # Only count frames if both hands present
    if left_hand and right_hand:
        # Forward / backward
        if left_hand['y_coord'] < acc_threshold - buffer:
            forward_frames += 1
            backward_frames = 0
        elif left_hand['y_coord'] > acc_threshold + buffer:
            backward_frames += 1
            forward_frames = 0
        else:
            forward_frames = 0
            backward_frames = 0

        # Left / right
        if right_hand['x_coord'] > steer_threshold + buffer:
            right_frames += 1
            left_frames = 0
        elif right_hand['x_coord'] < steer_threshold - buffer:
            left_frames += 1
            right_frames = 0
        else:
            left_frames = 0
            right_frames = 0
        print(f"fwd {forward_frames},  back {backward_frames}, left {left_frames}, right {right_frames}")
    else:
        left_frames = right_frames = forward_frames = backward_frames = 0

    # Holding logic
    if left_frames >= hold_threshold:
        hold_key('a')
    if right_frames >= hold_threshold:
        hold_key('d')
    if forward_frames >= hold_threshold:
        hold_key('w')
    if backward_frames >= hold_threshold:
        hold_key('s')

    # If none is held long enough, release any key
    elif (left_frames < hold_threshold and right_frames < hold_threshold and
          forward_frames < hold_threshold and backward_frames < hold_threshold):
        rels_key(('a','w','d','s'))

    cv.imshow("feed", image)
    if cv.waitKey(20) & 0xFF == ord('j'):
        break

vid.release()
cv.destroyAllWindows()

