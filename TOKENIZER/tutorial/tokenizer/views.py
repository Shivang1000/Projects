from django.shortcuts import render
from nltk.tokenize import *
from googletrans import Translator
# Create your views here.
def index(request):
    b=''
    a=''
    if request.method=='POST':
        un=request.POST.get('username')
        translator=Translator()
        rw=translator.translate(un, dest='hi')
        b= word_tokenize(rw.text)
        a="'"+"','".join(b)+"'"

    context={'token':a}
    return render(request,'show.html',context)