from django.shortcuts import render

# Create your views here.
def about(request):
    # return render(request,"about.html")
    return render(request,"navigation/about.html")

def contact(request):
#    return render(request,'contact.html')
   return render(request,"navigation/contact.html")