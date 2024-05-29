from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'author':'Rahim','age': 5,'lst':['python','is','best'],
         'birthday' :datetime.datetime.now(),'val' :'','courses' :[
        
        {
            'id': 1,
            'name':'python',
            'free':5000
        },
         {
            'id':2,
            'name':'javascript',
            'free':2000
        },

         {
            'id':3,
            'name':'html',
            'free':3000
        },
        ]}
    return render(request,'home.html',d)
