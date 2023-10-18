import speech_recognition as sr
import random
import json

def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_question(questions, difficulty):
    return random.choice(questions[difficulty])

def main():
    recognizer = sr.Recognizer()
    difficulty = 'easy'  # Start with easy questions
    score = 0  # Initialize score

    questions = load_questions('questions.json')

    while True:
        question = get_question(questions, difficulty)
        print(f'Tester: {question}')
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio, language='zh-CN')
            print(f'You: {response}')
            # TODO: Analyze the response using NLP, adjust difficulty, and update score
        except sr.UnknownValueError:
            print('Could not understand audio')

if __name__ == '__main__':
    main()