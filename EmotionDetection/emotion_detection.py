import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 200:
        formatted = json.loads(response.text)
        emotions = formatted['emotionPredictions'][0]['emotion']
        dominant = max(zip(emotions.values(), emotions.keys()))[1]
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant
        }
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    return result
