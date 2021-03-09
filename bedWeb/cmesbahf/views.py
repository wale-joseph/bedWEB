from django.shortcuts import render
from .forms import uploader
from django.http import HttpResponse

# Create your views here.


def handle_uploaded_file_path(f):
    stdout = 'bedApp/static/uploads'+f.name
    with open('bedApp/static/uploads'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return str(stdout)

def handle_uploaded_file(f):
    stdout = 'bedApp/static/uploads'+f.name
    with open('bedApp/static/uploads'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def x_y_editor(request):
    """
    converts the chromosome to a x-coordinate
    && genome position to the y-coordinates
    """
    import pandas as pd
    
    if request.method == 'POST':
        snpFile = uploader(request.POST, request.FILES)

        if snpFile.is_valid():
            #task = request.POST['task']
            df_file = handle_uploaded_file_path(request.FILES['fileOne'])
            df_file = pd.read_csv(str(df_file), sep=',')
            df_file['X_axis']= df_file['#CHR']+800
            df_file['Y_axis']= df_file['POS']+800
            
            response = HttpResponse(df_file, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=genome.csv'

            df_file.to_csv(path_or_buf=response)

            return response
    else:
        dataFile = uploader()
    return render(request, 'cmesbahf/genomics.html', {'form': dataFile})