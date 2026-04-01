from transformers import pipeline

def load_model():
    classifier = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    return classifier

def predict_sentiment(classifier, text):
    return classifier(text)