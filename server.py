from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Developing AI Applications with Python and Flask")

@app.route("/")
def home():
    # Simply render our index homepage
    return render_template('index.html')

@app.route("/emotionDetector")
def analyze_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    # Call out to the packaged function to analyze
    resp = emotion_detector(text_to_analyze)

    # Return the values as a formatted string
    return f"For the given statement, the system response is 'anger': {resp['anger']}, \
    'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']} and \
    'sadness': {resp['sadness']}. The dominant emotion is {resp['dominate_emotion']}."
        
