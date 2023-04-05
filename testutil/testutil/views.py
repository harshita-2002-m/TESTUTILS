from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello harshita</h1>  <a href="https://github.com/ArhamKhanPathan/SignUp-SignIn"> Github </a>''')
def index(request):
    # params= {'name': 'harry', 'place':'Mars'}
    
    return render(request, 'index.html')

def analyze(request):
    #get the text from the index.html
    djtext= request.POST.get('text','default')
    # print(djtext)
    #Check checkbox values
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    extraspaceremover= request.POST.get('extraspaceremover','off')
    charcount= request.POST.get('charcount','off')
    newlineremover= request.POST.get('newlineremover','off')

    #Check which checkbox is on
    if removepunc == "on":
        # analyzed= djtext
        punctuations= '''.,?!:;'"()[]-—.../\&@#$%^*+=<>|~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext= analyzed
        # return render(request, 'analyze.html', params)
    
    if (fullcaps =="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Change to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    
    if (extraspaceremover =="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        djtext= analyzed
        # return render(request, 'analyze.html', params)

    if (charcount =="on"):
        analyzed= 0
        for i in range(0,len(djtext)):
            if(djtext[i]) != ' ':
                analyzed = analyzed + 1
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed= ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            # else:
            #     print("no")
        print("pre",analyzed)
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        # djtext=analyzed

    if(removepunc!= "on" and fullcaps != "on" and extraspaceremover != "on" and charcount != "on" and newlineremover != "on"):
        return HttpResponse("Please select the operation and try again")
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")

    return render(request, 'analyze.html', params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("space remover")
# def charcount(request):
#     return HttpResponse("charcount")