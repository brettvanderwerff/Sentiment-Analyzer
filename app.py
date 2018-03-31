from flask import Flask, render_template, request, redirect, url_for, session, flash
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
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
Session(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/submission', methods = ['GET', 'POST'])
def submission():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
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

@app.errorhandler(413)
def page_not_found(e):
    return "Your error page for 413 status code", 413

if __name__ == '__main__':
   app.run(debug=True)
