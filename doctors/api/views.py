from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import DoctorSerializer
import pandas as pd
# Create your views here.
df = pd.read_excel('doctors.xls')
arr=['Alcoholism Treatment  ', 'Algologists (Pain Specialists)  ',
       'Allergy   ', 'Anaesthesiology  ',
       'Cardiology (Heart Specialists)  ', 'General Medicine  ',
       'Doctors- Neurologist  ', 'Doctors- General Medicine  ',
       'Doctors- Obstetrics & Gynaecology  ', 'Doctors- Psychologists  ',
       'Doctors- Neuro Psychiatrist  ']

def system(disease):
    disease= disease.lower()
    for i in arr:
        
        if disease in i.lower():
         
            print('----------------------------------------------')
            print(df[df.Category=='Allergy   '].values.tolist())
            print('----------------------------------------------')
    else:
        print("no")

class doctors(APIView):
    serializer_class = DoctorSerializer
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
             
                disease= serializer.validated_data.get("disease")
                disease= disease.lower()
                val=[]
                for i in arr:                   
                    if disease in i.lower():
                        val=(df[df.Category==i].values.tolist())
                        break
                
               
                return Response({'list':val}, status=status.HTTP_200_OK)
        else:
                
                return Response({"status": "failed", "message": "in else"}, status=status.HTTP_400_BAD_REQUEST)

