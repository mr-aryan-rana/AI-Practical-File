from transformers import pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    tokenizer="distilbert-base-uncased-finetuned-sst-2-english"
)
texts = [
    "I'm so excited about this new technology!",
    "The quality is poor and I want a refund.",
    "It's decent but could be better."
]

results = sentiment_pipeline(texts)

for text, result in zip(texts, results):
    print(f"Text: {text}")
    print(f"Label: {result['label']}, Score: {result['score']:.4f}")
    print("-" * 50)