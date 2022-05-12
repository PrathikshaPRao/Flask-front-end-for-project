from flask import Flask, render_template, redirect,url_for, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        #return "File has been uploaded."
        return redirect(url_for('patientData'))
    return render_template('index.html', form=form)

@app.route('/patientData', methods=['GET',"POST"])
def patientData():
    if request.method == "POST":
       
       occOfPain = request.form.get("occOfPain")
      
       bloodReportStat = request.form.get("bloodReportStat") 
       return "Patient Details "+occOfPain+"  " + bloodReportStat
    return render_template("form.html")
  

def patientData1():
   return 'logged in successfully'
if __name__ == '__main__':
    app.run(debug=True)