from flask import Flask, render_template
import os
from flask import flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'templates/assets/uploads'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

app=Flask(__name__,static_folder="templates/assets")

app.config['SECRET_KEY']='mysecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadimg', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            import check
            predict=check.image_mod(filename)
            return render_template('upload.html',predict=predict,imgpath='assets/uploads/'+filename)
            #return redirect(url_for('uploaded_file',filename=filename))
    return  render_template('upload.html',predict="",imgpath="assets/img/Designer (4).png")
    #return  render_template('output.html',predict="")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    import check
    predict=check.image_mod(filename)
    return render_template('upload.html',predict=predict)
    #return render_template('output.html',predict=predict)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return redirect(url_for('upload_file'))
    #return render_template('upload.html')

if __name__=="__main__":
    app.run()
    
    

