import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)
    return format_response(response.json())

def format_response(response_json):
    emotions = response_json['emotionPredictions'][0]['emotion']
    emotions['dominate_emotion'] = max(emotions, key=emotions.get)
    return emotions

def find_dominate_emotion(emotions):
    return max(emotions, key=emotions.get)