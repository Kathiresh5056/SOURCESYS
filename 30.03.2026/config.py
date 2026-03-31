from transformers import pipeline

def load_model():
    generator = pipeline(
        "text-generation",
        model="distilgpt2"   # lightweight & fast
    )
    return generator