# -*- coding: utf-8 -*-

import imutils
import cv2
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pdf2image import convert_from_path
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from transformers import pipeline

import os
JAVA_HOME = r"C:\Program Files\Java\jdk1.8.0_144\bin\java.exe"
os.environ.setdefault('JAVA_HOME', JAVA_HOME)
# initialize pipline
print("[INFO] loading NER Model ...")
pipe = pipeline("ner", model="src/Arabic_model_trained", device=0)

st = StanfordNERTagger('src/stanford-ner-2020-11-17/classifiers/english.muc.7class.distsim.crf.ser.gz',
					   'src/stanford-ner-2020-11-17/stanford-ner.jar',
					   encoding='utf-8')

nltk.download('punkt')
print("[INFO] loading face detector...")
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def pdf_to_image(pdfPath,outPath):
    '''
    INPUTS:-
        pdfPath: the path to the PDF file
        outPath: the output path for images in the PDF file "Must End with \"

    OUTPUTS:-
        Paths: list of the paths of the Images
    '''
    paths=[]
    images = convert_from_path(pdfPath, 500)
    for i, image in enumerate(images):
        fname = 'image '+str(i)+'.png'
        image.save(outPath+fname, "PNG")
        paths.append(outPath+fname)
    return paths


def process_audio(pathfile,outPath,min_silence_len=500,silence_thresh=-40):
    paths=[]
    #reading from audio mp3 file
    sound = AudioSegment.from_mp3(pathfile)
    # spliting audio files
    audio_chunks = split_on_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh )
    #loop is used to iterate over the output list
    for i, chunk in enumerate(audio_chunks):
        output_file = outPath+"{0}_chunck.mp3".format(i)
        print("Exporting file", output_file)
        chunk.export(output_file, format="mp3")
        paths.append(output_file)
    return paths

def process_photo(file,outPath,scaleFactor=1.05,minNeighbors=12,minSize=(30, 30)):
    
    image = cv2.imread(file)
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector.detectMultiScale(gray, scaleFactor=scaleFactor,
        minNeighbors=minNeighbors, minSize=minSize,
        flags=cv2.CASCADE_SCALE_IMAGE)

    print("[INFO] {} faces detected...".format(len(rects)))
    for (x, y, w, h) in rects:
        # draw the face bounding box on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print("writing the image with a bounding box on the face")
    cv2.imwrite(outPath+'imageWithFaces.jpeg', image)
    return len(rects),rects,outPath+'imageWithFaces.jpeg'
        


def process_text(text,language):
    returned_words=[]
    if language == 'EN':
        
        tokenized_text = word_tokenize(text)
        classified_text = st.tag(tokenized_text)
        for pred in classified_text:
            if pred[1] !='O':
                returned_words.append(pred)
        return returned_words 
    else :
        labels={'B-LOC': 0, 'O': 1, 'B-PERS': 2, 'I-PERS': 3, 'B-ORG': 4, 'I-LOC': 5, 'I-ORG': 6, 'B-MISC': 7, 'I-MISC': 8}
        for prediction in pipe(text):
            label_ind=prediction['entity'].split('_')[1]
            label=list(labels.keys())[list(labels.values()).index(label_ind)]
            if label != 'O':
                returned_words.append((prediction['word'],label))
        return returned_words





#pdf_to_image("E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_pdf.pdf","src/")
#process_photo("E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_image.png","src/")
#re=process_text("Hello USA","EN")
#print(re)
#process_audio('E:/ML/FreeLance/intalio/mle-challenge/tests/static/test_audio.mp3','src/')

print("end")


