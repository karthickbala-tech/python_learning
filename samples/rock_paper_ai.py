import cv2
import mediapipe as mp
import numpy as np
import random
import joblib

# Load trained model
model = joblib.load('gesture_model.pkl')

# Score setup
MAX_SCORE = 3
user_score = 0
ai_score = 0

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Basic dummy feature extractor (simulate from landmark)
def get_prediction(landmarks):
    # Dummy: use the first 3 landmarks as features
    features = np.array([[lm.x, lm.y, lm.z] for lm in landmarks]).flatten()[:9]
    features = features.reshape(1, -1)
    try:
        return model.predict(features)[0]
    except:
        return "unknown"

def ai_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def check_winner(user, ai):
    if user == ai:
        return "draw"
    elif (user == "rock" and ai == "scissor") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissor" and ai == "paper"):
        return "user"
    else:
        return "ai"

# Start webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    game_started = False
    print("👋 Show your hand to start the game!")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if not game_started:
                    game_started = True
                    print("🎮 Game Started!")

                user_move = get_prediction(hand_landmarks.landmark)
                ai_move = ai_choice()

                winner = check_winner(user_move, ai_move)

                if winner == "user":
                    user_score += 1
                elif winner == "ai":
                    ai_score += 1

                # Display moves and score
                cv2.putText(frame, f"You: {user_move}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"AI: {ai_move}", (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                cv2.putText(frame, f"Score - You: {user_score}  AI: {ai_score}", (10, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                # Game over
                if user_score == MAX_SCORE or ai_score == MAX_SCORE:
                    result_text = "🎉 You Win!" if user_score == MAX_SCORE else "😢 AI Wins!"
                    cv2.putText(frame, result_text, (100, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                    cv2.imshow("Rock Paper Scissors", frame)
                    cv2.waitKey(3000)
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

        cv2.imshow("Rock Paper Scissors", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
