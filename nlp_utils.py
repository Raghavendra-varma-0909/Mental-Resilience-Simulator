from textblob import TextBlob

def score_reflection(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return 2
    elif polarity > 0:
        return 1
    elif polarity == 0:
        return 0
    else:
        return -1