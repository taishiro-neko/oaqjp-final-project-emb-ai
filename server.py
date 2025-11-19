''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it. The output returned shows 
        the list of emotions with their scores, and the dominant
        emotion.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    dominant = response["dominant_emotion"]

    if not dominant:
        return "Invalid text! Please try again!"


    # Skip the dominant_emotion key
    emotion_parts = [
        f"'{k}': {v}"
        for k, v in response.items()
        if k != "dominant_emotion"
    ]

    # Assuming there's always at least 2 emotions:
    emotion_str = ", ".join(emotion_parts[:-1]) + " and " + emotion_parts[-1]

    result = (
        f"For the given statement, the system response is {emotion_str}. "
        f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
    )

    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
