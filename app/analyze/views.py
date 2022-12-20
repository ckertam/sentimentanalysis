from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
# Create your views here.
from textblob import TextBlob
import os
class AnalyzeTweetsAPIView(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        sentences = data.get("tweets")
        username = data.get("username")
        since_date = data.get("since_date")
        polarity=0.0
        subjectivity=0.0
        for sentence in sentences:
            res = TextBlob(sentence)
            polarity += res.sentiment.polarity
            subjectivity += res.sentiment.subjectivity
        avg_polarity = polarity/float(len(sentences))
        avg_subjectivity = subjectivity/float(len(sentences))
        happiness_value = "unhappy"
        subjectivity_value = "objective"
        if avg_polarity > 0:
            happiness_value = "happy"
        if avg_subjectivity > 0:
            subjectivity_value="subjective"
        

        response = f"{username} is {happiness_value} and {subjectivity_value} since {since_date}"
        return Response(response, status=200)

class AnalyzeTweetsSimulationAPIView(APIView):
    def post(self,request,*args,**kwargs):
        data = request.data
        username = data.get("username")
        since_date = data.get("since_date")
        file_path = os.path.abspath("analyze/TestExcel.xlsx")
        df = pd.read_excel(file_path)
        sentences=df["tweet"].values.tolist()
        polarity=0.0
        subjectivity=0.0
        for sentence in sentences:
            res = TextBlob(sentence)
            polarity += res.sentiment.polarity
            subjectivity += res.sentiment.subjectivity
        avg_polarity = polarity/float(len(sentences))
        avg_subjectivity = subjectivity/float(len(sentences))
        happiness_value = "unhappy"
        subjectivity_value = "objective"
        if avg_polarity > 0:
            happiness_value = "happy"
        if avg_subjectivity > 0:
            subjectivity_value="subjective"
        
        response = f"{username} is {happiness_value} and {subjectivity_value} since {since_date}"
        return Response(response, status=200)

