from django.shortcuts import render

from service.models import Service


def comer(request):
   try:
        if request.method=='POST':
            comment =(request.POST.get('n1'))
            y=Service( comment=comment) 
            y.save()  
   except:
        pass         
   return render(request,'image.html')
 

  