import requests 
import json

def emotion_detector(text_to_analyse):  
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 400:  # blank input or some other error
        return {"dominant_emotion": None}

    formatted_response = json.loads(response.text)
    #pretty_json = json.dumps(formatted_response, indent=4)
    #print (pretty_json)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions

