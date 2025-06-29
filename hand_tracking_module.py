import cv2 as cv
import mediapipe as mp
import time

class hand_detection():                         
    def __init__(self, mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5): 
        self.mode = mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_num_hands,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.results = None

    def detection(self, image, draw=True):         
        rgbimg = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(rgbimg)

        if self.results.multi_hand_landmarks:      
            for hand_landmarks in self.results.multi_hand_landmarks:      
                if draw:     
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image


    def find_position(self, image, draw=True):

        allHands = []
        if self.results.multi_hand_landmarks:
            h, w, c = image.shape
            for hand_landmarks in self.results.multi_hand_landmarks:
                x_coords = []
                landmark_list = []
                
                for id, lm in enumerate(hand_landmarks.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cz = int(lm.z * w)
                    x_coords.append(cx)
                    landmark_list.append((id, cx, cy, cz))
                
                x_avg = sum(x_coords) / len(x_coords)
                if x_avg < w//2:
                    hand_index = 0
                    color = (0, 255, 0)  # Green for left hand
                else:
                    hand_index = 1
                    color = (255, 0, 0)  # Blue for right hand

                for id, cx, cy, cz in landmark_list:
                    cv.circle(image, (cx, cy), 7, color, cv.FILLED)

                allHands.append(
                    {'index': hand_index, 'landmarks': landmark_list}
                )
        return allHands



def main():
    vid = cv.VideoCapture(0)
    currentTime = 0
    previousTime = 0
    detector = hand_detection()

    while True:
        isTrue, frame = vid.read()
        frame = cv.flip(frame,1)
        image = detector.detection(frame)
        landmarks = detector.find_position(image)
        height, width = image.shape[:2]
        if landmarks:
            # Loop over each detected hand
            for hand in landmarks:
                index = hand['index']  # 0 = left, 1 = right
                landmarks = hand['landmarks']
                print(f"Hand {index} landmarks:")
                for lm in landmarks:
                    print(lm)  # lm = (id, cx, cy, cz)
        
        center = (width // 2, height // 2)
        cv.circle(frame, center, radius=200, color=(0, 0, 225), thickness=3)
        cv.line(frame, (320, 40), (320, 440), (0, 225, 0), 5)
        cv.line(frame, (120, 240), (520, 240), (225, 0, 0), 5)
        
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        cv.putText(image, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (25, 7, 5))
        cv.imshow('cam feed', image)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    vid.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
