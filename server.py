''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and their
        confidence score and the dominant emotion for the provided text.
    '''
    text = request.args.get('textToAnalyze')
    res = emotion_detector(text)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {res['anger']}, 'disgust': "
        f"{res['disgust']}, 'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': "
        f"{res['sadness']}. The dominant emotion is {res['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
