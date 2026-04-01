from model.sentiment_model import load_model, predict_sentiment
from utils.helper import get_user_input

def main():
    print("=== Sentiment Analysis App ===")
    
    # Load model
    classifier = load_model()
    
    while True:
        text = get_user_input()
        
        if text.lower() == "exit":
            print("Exiting...")
            break
        
        result = predict_sentiment(classifier, text)
        print(f"Sentiment: {result[0]['label']} (Score: {result[0]['score']:.4f})\n")

if __name__ == "__main__":
    main()