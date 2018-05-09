# Sentiment-Analysis-Flask-App


~~~~~~~
About:
~~~~~~~
A website that does simple sentiment analysis and word cloud production using vaderSentiment (https://github.com/cjhutto/vaderSentiment/tree/master/vaderSentiment) and word_cloud (https://github.com/amueller/word_cloud). This website was created as way to practice developing a Flask app and then deploying the app to a web server. This project is still in developemt.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirements to run locally:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Flask_WTF==0.14.2

matplotlib==2.1.0

requests==2.18.4

WTForms==2.1

Flask==0.12.2

nltk==3.2.5

vaderSentiment==2.5

wordcloud==1.4.1

Flask-Session==0.3.1

You may also find yourself needing to set up a C compiler if you machine does not already have this, word_cloud requires a C compiler to run.

~~~~~~~~
Useage: 
~~~~~~~~

The app gives you the choice of uploading a txt document or submitting text in a word field for analysis. Text documents must be UTF-8 encoded and be under 1 megabyte. Currently there is no database on the backend. User submitted documents are stored server side in temporary files using the Flask extension: Flask-Session (https://pythonhosted.org/Flask-Session/). I plan to incorperate a databse once I learn SQL. Once analysis is complete, the most positive and negative sentences of the document (accoring to vaderSentiment(https://github.com/cjhutto/vaderSentiment/tree/master/vaderSentiment)) are rendered back the the user. A word cloud that is generated using all words of the original document is also rendered using word_cloud (https://github.com/amueller/word_cloud). 

~~~~~~~~~~~~~~~~
Quality control:
~~~~~~~~~~~~~~~~

Seems to perform well on windows 10 with Python 3.7 and Ubuntu 16.04 with Python 3.5. I have not tried the program with any other setups. 




