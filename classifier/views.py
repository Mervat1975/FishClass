
from django.shortcuts import render
import pandas as pd
import joblib
import os


# Create your views here.


def PredictSpecies(Weight, Length1, Length2, Length3, Height, Width):
    input = pd.DataFrame({
        'Weight': [Weight],
        'Length1,': [Length1],
        'Length2': [Length2],
        'Length3': [Length3],
        'Height': [Height],
        'Width': [Width]
    })
    loaded_rf = joblib.load(os.path.join("./random_forest.joblib"))
    out = loaded_rf.predict(input)
    return(out)


def classifier(request):
    if request.method == 'GET':
        result = "none"
        return render(request, 'index.html', {'result': result})
    elif request.method == 'POST':
        post_data = request.POST
        weight = int(post_data.get('weight'))
        length1 = int(post_data.get('length1'))
        length2 = int(post_data.get('length2'))
        length3 = int(post_data.get('length3'))
        width = int(post_data.get('width'))
        height = int(post_data.get('height'))
        result = PredictSpecies(
            weight, length1, length2, length3, height, width)
        result = str(result).replace("'", "").replace("[", "").replace("]", "")
        return render(request, 'index.html', {'result': result, 'weight': weight, 'length1':
                                              length1, 'length2': length2, 'length3': length3,
                                              'height': height, 'width': width})
