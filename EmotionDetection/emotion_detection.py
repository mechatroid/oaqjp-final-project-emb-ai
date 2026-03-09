import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)    

    # If the status code is 200, extract the emotion scores
    if response.status_code == 200:
        # Extracts the emotion scores and stores them in variables
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score =  formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # If the response status code is 400, set the emotion scores to None
    elif response.status_code == 400:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_sentiment = None
        return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_sentiment
        }
    
    # Compile the emotion scores into a dictionary
    sentiment_data = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    # Calculate the dominant emotion and extract its name (key)
    dominant_sentiment = max(sentiment_data, key = sentiment_data.get)
    dominant_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_sentiment
    }