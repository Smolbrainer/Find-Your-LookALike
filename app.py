import cv2
import numpy as np
import face_recognition as fr
import os
import sqlite3
import flask
from shutil import copyfile

app = flask.Flask(__name__)
app.secret_key = 'supersecretkey'

#Retrieves the data from the server and sends it back to the server for processing
@app.route('/', methods=['GET', 'POST'])
def index():
        #Encodes the image that was uploaded then saves it in the session
        if flask.request.method == 'POST':
            if 'file' not in flask.request.files:
                  return flask.redirect('/')
            file = flask.request.files['file']
            img = fr.load_image_file(file)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

            encodings = fr.face_encodings(img)
            if not encodings:
                return flask.render_template('index.html', error="No face detected. Try another image.")
            encoding1 = encodings[0]

            flask.session['encoding1'] = encoding1.tolist()

            return flask.redirect('/redirection')
        return flask.render_template('index.html')

@app.route('/redirection')
def loadImg():
    #Finds the most similar image in the database based on the closes encodings and then sends it back to html
    encoding1 = flask.session.get('encoding1')
    if encoding1 is None:
        return flask.redirect('/')
    
    con = sqlite3.connect("encodings.db")
    db = con.cursor()
    db.execute("SELECT image_path, encoding FROM encodings")
    stored_encodings = db.fetchall() 

    #Loops through every tuple in stored_encodings and compares it with the encoding of the uploaded file using cosine similarity
    max = -1
    for image_path, encoding_blob in stored_encodings:
        stored_encoding = np.frombuffer(encoding_blob, dtype=np.float64)
        distance = np.dot(stored_encoding, encoding1) / (np.linalg.norm(stored_encoding) * np.linalg.norm(encoding1))  
        if max<distance: 
            max = distance
            mostImg = image_path

    con.close()

    #Copies the file to a folder called static
    copyfile(mostImg, "./static/image.jpg")

    return flask.render_template('redirection.html', max=max, mostSim=mostImg)



#Old code that was used for testing

# mainImgDir = 'horse.jpeg'.upper()
# imgLebron = fr.load_image_file(f"Lebron_tests/{mainImgDir}")

# imgLebron = fr.load_image_file(file)
# imgLebron = cv2.cvtColor(imgLebron,cv2.COLOR_BGR2RGB)

#Found the location of a face in an image then drew a rectangle around it

#facelocation = fr.face_locations(imgLebron)
#top, right, bottom, left = facelocation[0]
#cv2.rectangle(imgLebron, (left, top), (right, bottom), (0, 255, 0), 3)

# mostSim = fr.load_image_file(mostImg)
# mostSim = cv2.cvtColor(mostSim,cv2.COLOR_BGR2RGB)
# print(f"You are most similar to {mostImg}")
# print(f"Facial similarity score: {max}")
# cv2.imshow('Similar Img', mostSim)
# cv2.imshow('Img', imgLebron)
# cv2.waitKey(0)
