from django.shortcuts import render
from django.http import HttpResponse

from .forms import MakeShortForm, GetLongForm

def home(request):
    return HttpResponse("Hello, world. You're at the urlShortener home.")

def makeShort(request):
    if request.method == 'POST':
        makeForm = MakeShortForm(request.POST)
        if makeForm.is_valid():
            input_from_form = makeForm.cleaned_data
            res = input_from_form['longUrl']*3
            return render(request, "template.html", {
                'form':MakeShortForm(request.POST),
                'output_result': res,
                'res_label': "Short URL:"
                })
    else:
        return render(request, 'template.html', {
            'form':MakeShortForm()
            })
    # return HttpResponse("Hello, world. You're at the makeShort.")

def getLong(request):
    if request.method == 'POST':
        getForm = GetLongForm(request.POST)
        if getForm.is_valid():
            input_from_form = getForm.cleaned_data
            res = input_from_form['shortUrl']*3
            return render(request, "template.html", {
                'form':GetLongForm(request.POST),
                'output_result': res,
                'res_label': "Long URL:"
                })
    else:
        return render(request, 'template.html', {
            'form':GetLongForm()
            })
    # return HttpResponse("Hello, world. You're at the getLong.")

def urlRedirector(request,urlHash):
    return HttpResponse(f"Hello, world. You're at the urlRedirector with hash {urlHash}.")
