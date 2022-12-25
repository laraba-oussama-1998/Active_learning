from django.shortcuts import render
from django.http import HttpResponse
from .utils import load_data_to_predict
from .apps import CharAlConfig
from sklearn.metrics import accuracy_score
import json
# Create your views here.

def home(request):
    
    context = {}
    if request.method == 'POST' and request.FILES['Datafile']:
        file = request.FILES['Datafile']
        
        Data, labels = load_data_to_predict(file, CharAlConfig.headers, CharAlConfig.labelEncoder)
        predictions = CharAlConfig.classifier.predict(Data)
        acc_score = accuracy_score(predictions, labels)
        
        result_dict = {}
        data = []
        
        labels = CharAlConfig.labelEncoder.inverse_transform(labels)
        predictions = CharAlConfig.labelEncoder.inverse_transform(predictions)
        
        for index, pred in enumerate(predictions):
            result_dict[index+1]= [labels[index], pred]
            data.append(Data[index].tolist())
        
        return render(request, 'char_al/results.html', {
            'acc_score': round(acc_score*100,2),
            'result_dict': result_dict, 
            'data': json.dumps(data),
            'headers': json.dumps(CharAlConfig.headers)
            })
    
    return render(request, 'char_al/home.html')
    

    