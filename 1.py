from flask import Flask, render_template
from flask import jsonify
import os
import flask
import werkzeug
import numpy
import scipy.misc
import os.path
from omr2 import omr2
import base64

app = Flask(__name__, static_url_path='/static/')
@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    '''
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    '''
    imageresult = omr2("D:/Data/kuliah/TA-doc/Code/FinalCopy/androidFlask.jpg")
    path = r'D:\Data\kuliah\TA-doc\Code\FinalCopy\static'
    data_uri = base64.b64encode(open('detected.png', 'rb').read()).decode('utf-8')
    img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

    '''
    return rv
    
    imageresult = omr2("D:/Data/kuliah/TA-doc/Code/FinalCopy/androidFlask.jpg")
    imageresult.save("static/detected.png", "PNG")
    with open(static,"rb") as imageresult:
        encoded_string=base64.b64encode(imageresult.read())
    '''
    return flask.jsonify(data_uri)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)