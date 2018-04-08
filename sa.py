from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from form import MyForm
from logging import FileHandler, WARNING
import text_analysis

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt') #file_handler logs errors
file_handler.setLevel(WARNING)
app.config.from_object(__name__) # Config for Flask-Session

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 #max upload size is 1MB
app.config['SECRET_KEY'] = 'secret'
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])#restricts file extensions to the .txt extension
app.config['SESSION_TYPE'] = 'filesystem' #config for Flask Session, indicates will store session data in a filesystem folder
app.logger.addHandler(file_handler)
Session(app) #create Session instance

def allowed_file(filename):
    '''Checks uploaded file to make sure it is.txt'''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        session['file_contents'] = form.name.data
        return redirect('/analysis')
    return render_template('submit.html', form=form)

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            session['file_contents'] = file.read().decode('utf-8')
            return redirect(url_for('analysis'))
    return render_template('upload.html')

@app.route('/analysis')
def analysis():
    file_contents = session.get('file_contents')
    analyzed_sent = text_analysis.get_pos_neg(file_contents)
    pos_sent = analyzed_sent[-1]
    neg_sent = analyzed_sent[0]
    word_cloud = text_analysis.render_word_cloud(file_contents)
    return render_template('analysis.html', pos_sent=pos_sent, neg_sent=neg_sent, word_cloud=word_cloud)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
   app.run()
