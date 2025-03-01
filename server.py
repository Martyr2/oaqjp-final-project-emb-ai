"""
This Flask web application provides an interface for analyzing emotions in 
text using the EmotionDetection package. It includes routes for rendering 
the homepage and processing emotion detection requests.

Routes:
- `/` : Renders the homepage (`index.html`).
- `/emotionDetector` : Accepts a text query parameter, analyzes its 
emotion using `emotion_detector`, and returns the detected emotions.

Example Output:
    For the given statement, the system response is 'anger': 0.01, 'disgust': 0.02, 
    'fear': 0.05, 'joy': 0.90 and 'sadness': 0.02. The dominant emotion is 'joy'.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Developing AI Applications with Python and Flask")

@app.route("/")
def home():
    """Simply render our index homepage"""
    return render_template('index.html')

@app.route("/emotionDetector")
def analyze_emotion():
    """Takes in the text to analyze and returns a statement score the emotion involved."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Call out to the packaged function to analyze
    resp = emotion_detector(text_to_analyze)

    # If reply came back with dominate emotion is None, show error to user
    if resp['dominate_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return the values as a formatted string
    return f"For the given statement, the system response is 'anger': {resp['anger']}, \
    'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and \
    'sadness': {resp['sadness']}. The dominant emotion is {resp['dominate_emotion']}."