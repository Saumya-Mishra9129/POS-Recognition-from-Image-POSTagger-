from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import nltk
import shutil


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    arr = list(text.split())
    return arr




def processContent(exampleArray):
    try:
        if('pos.txt'):
            open('pos.txt','w').close()

        for item in exampleArray:
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)

            file_create(tagged)
            #print(tagged)


    except Exception as e:
        print(str(e))

def path_to(path):
    exampleArray = list(ocr_core(path))
    processContent(exampleArray)
def file_create(tagged):

    file = open('pos.txt', 'a')
    for each in tagged:
        file.write(each[0] + " " + each[1])
        file.write("\n")
    file.close()




class Home(TemplateView):
    template_name = 'home.html'


def generate(request):
    searchWord = request.GET.get('search')
    path='/home/saumya/POSTagger/media/'+str(searchWord)
    path_to(path)
    file=open('pos.txt','r')
    content=file.read()
    file.close()


    return HttpResponse(content,content_type='text/plain')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)



    return render(request, 'upload.html', context)



