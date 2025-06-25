from django.shortcuts import render
def index(request): 
    return render(request , 'index2.html')


def preprocess(request): 
    text  = request.POST.get('text' , 'default')
    punc = request.POST.get('punc' , 'of')
    cap = request.POST.get('cap' , 'of')
    original = text
    if punc == 'on': 
        processed_text = ''
        punctuations = ''''!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~' ''' 
        for char in text: 
            if char not in punctuations: 
                processed_text += char
        text = processed_text
    if cap == 'on': 
        text = text.upper()
    counter = request.GET.get('counter' , 'off')
    params = { 
        'original_text' : original, 
        'processed_text' : text

    }
    if counter == 'on': 
        char_count = len(text)  # Or you can use a loop like before
        params['Total_characters'] = char_count

    return render(request, 'preprocess2.html', params)

def about_Us(request): 
    return render(request , 'about_Us.html')

def contact_Us(request): 
    return render(request , 'contact_Us.html')
