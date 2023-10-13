"""
This module contains the Flask server for the emotion detection application.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    """
    Handles the emotion detection route in the Flask app.
    """
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"})

    response_text = (
    f"For the given statement, the system response is 'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
    f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
