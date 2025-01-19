#Loads all the encodings into a dataset.

# import sqlite3
# import face_recognition as fr
# import cv2
# import os
# import numpy as np
# con = sqlite3.connect("encodings.db")
# db = con.cursor()

# DIR = './images2'
# max = 100
# for i in os.listdir(DIR):
#         img_path = os.path.join(DIR,i)
#         img = fr.load_image_file(img_path)
#         img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         try:
#             encoding = fr.face_encodings(img)[0]
#             encoding_bytes = np.array(encoding).tobytes()
#             db.execute("INSERT INTO encodings (image_path, encoding) VALUES (?, ?)", (img_path, encoding_bytes))
#         except:
#              os.remove(img_path)
#         print(i)

# con.commit()
# con.close()

# print("Encoding process complete!")