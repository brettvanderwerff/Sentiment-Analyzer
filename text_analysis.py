import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def text_analysis(corpus):

    sentences = nltk.sent_tokenize(corpus)
    analyzer = SentimentIntensityAnalyzer()
    result = {sentence: analyzer.polarity_scores(sentence) for sentence in sentences}
    sorted_result = sorted(result, key=lambda x: result[x]['compound'])
    return [sorted_result[0], sorted_result[-1]]

def main(file_contents):
    return text_analysis(file_contents)



