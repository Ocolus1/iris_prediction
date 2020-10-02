from django.shortcuts import render
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
from sklearn.datasets import load_iris
from django.http import JsonResponse
from .models import PredResults


def index(request):
    context = {}
    return render(request, "iris/index.html", context)


def predict_chances(request):
    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=0.20, random_state=1)

    # Fitting the model
    model = SVC(gamma="auto")
    model.fit(X_train, Y_train)

    if request.POST.get("action") == "post":

        # Recieve data from the client
        sepal_length = float(request.POST.get("sepal_length"))
        sepal_width = float(request.POST.get("sepal_width"))
        petal_length = float(request.POST.get("petal_length"))
        petal_width = float(request.POST.get("petal_width"))

        result = model.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]])

        classification = "Iris-{}".format(iris.target_names[result][0])

        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width,
                                petal_length=petal_length, petal_width=petal_width, 
                                classification=classification)

        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def results(request):
    context = {"dataset": PredResults.objects.all().order_by("-id")}
    return render(request, "iris/results.html", context)
