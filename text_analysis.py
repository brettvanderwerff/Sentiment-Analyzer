import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud

def get_pos_neg(corpus):
    '''Returns the most positive and negative sentences of the corpus.
    '''
    nltk.download('punkt')
    sentences = nltk.sent_tokenize(corpus)
    analyzer = SentimentIntensityAnalyzer()
    result = {sentence: analyzer.polarity_scores(sentence) for sentence in sentences}
    sorted_result = sorted(result, key=lambda x: result[x]['compound'])
    return [sorted_result[0], sorted_result[-1]]

def render_word_cloud(corpus):
    '''Generates a word cloud using all the words in the corpus.
    '''
    fig_file = BytesIO()
    wordcloud = WordCloud(max_font_size=40, background_color='white').generate(corpus)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(fig_file, format='png')
    fig_file.seek(0)
    fig_data_png = fig_file.getvalue()
    result = base64.b64encode(fig_data_png)
    return result.decode('utf-8')



