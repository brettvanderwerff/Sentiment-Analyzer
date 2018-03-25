from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import text_analysis

#restricts file extensions to the .txt extension
ALLOWED_EXTENSIONS = set(['txt'])
#config for Flask Session, indicates will store session data in a filesystem folder
#(https://pythonhosted.org/Flask-Session/)
SESSION_TYPE = 'filesystem'

app = Flask(__name__)
app.config.from_object(__name__)
# create Session instance
Session(app)

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/submission', methods = ['GET', 'POST'])
def submission():
    if request.method == 'POST':
        file = request.files['file']
        session['file_contents'] = file.read()
        return redirect(url_for('analysis'))
    return render_template('submission.html')

@app.route('/analysis')
def analysis():
    file_contents = session.get('file_contents', None)
    analyzed_sent = text_analysis.main(file_contents=file_contents)
    pos_sent = analyzed_sent[-1]
    neg_sent = analyzed_sent[0]
    return render_template('analysis.html', pos_sent=pos_sent, neg_sent=neg_sent)


if __name__ == '__main__':
   app.run(debug=True)