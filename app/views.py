from django.shortcuts import render
from app.models import TextUpload
import pickle
import joblib
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

import os

# Create your views here.

def prediction(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        

        tags = ['\n', '\'']
        for tag in tags:
            text = text.replace(tag, '')

        text = [str(text)]
        model = joblib.load('app/model/model.pkl')
        vectorizer = joblib.load('app/model/vectorizer.pkl')

        pre = model.predict(vectorizer.transform(text))

        print(pre[0])

        if text:
            if pre[0] == 1.0:
                desc = 'Last Text was: '
                pred = 'AI Generated'
                color = '#6495ED'
            elif pre[0] == 0.0:
                desc = 'Last Text was: '
                pred = 'Human Generated'
                color = '#50C878'
            else:
                desc = 'Re-Enter the Text'
                pred = 'Error'
                color = '#FF5733'
    else: 
        desc = 'Version: 1'
        pred = 'Enter Text'
        color = '#3C6478'

    s_text = str(text)
    s_text = s_text.replace('\r', '↵')



    context = {'prediction':pred, 'color':color, 'desc':desc, 'text':s_text}
        
    return render(request, 'home.html', context)
