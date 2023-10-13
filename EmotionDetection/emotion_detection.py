import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    PAYLOAD = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(URL, headers=HEADERS, json=PAYLOAD)

        if response.status_code == 200:
            data = response.json()

            emotions = data['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)

            output = {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness'],
                'dominant_emotion': dominant_emotion
            }

            return output
        elif response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"
