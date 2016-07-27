from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
from nltk.sentiment import SentimentIntensityAnalyzer

class Sentiment():
    @staticmethod
    def demo_liu_hu_lexicon(sentence):
        """
        Basic example of sentiment classification using Liu and Hu opinion lexicon.
        This function simply counts the number of positive, negative and neutral words
        in the sentence and classifies it depending on which polarity is more represented.
        Words that do not appear in the lexicon are considered as neutral.

        :param sentence: a sentence whose polarity has to be classified.
        :param plot: if True, plot a visual representation of the sentence polarity.
        """

        tokenizer = treebank.TreebankWordTokenizer()
        pos_words = 0
        neg_words = 0
        tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

        x = list(range(len(tokenized_sent))) # x axis for the plot
        y = []

        for word in tokenized_sent:
            if word in opinion_lexicon.positive():
                pos_words += 1
                y.append(1) # positive
            elif word in opinion_lexicon.negative():
                neg_words += 1
                y.append(-1) # negative
            else:
                y.append(0) # neutral

        if pos_words > neg_words:
            return 'Positive'
        elif pos_words < neg_words:
            return 'Negative'
        elif pos_words == neg_words:
            return 'Neutral'

    @staticmethod
    def demo_vader_instance(text):
        """
        Output polarity scores for a text using Vader approach.

        :param text: a text whose polarity has to be evaluated.
        """
        vader_analyzer = SentimentIntensityAnalyzer()
        return vader_analyzer.polarity_scores(text)
