from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from .forms import uploaderOne, uploaderTwo
import subprocess
import csv
import sys
from .models import Table


#upload handler
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
    

# Create your views here.

def oneFile(request):

    if request.method == 'POST':
        dataFile = uploaderOne(request.POST, request.FILES)
        
        if dataFile.is_valid():
            task = request.POST['task']
            outOne = handle_uploaded_file_path(request.FILES['fileOne'])
            with open('bedApp/static/uploads/temp', "w+") as f:
                outputOne = subprocess.run(['bedtools', task, '-i', outOne], stdout=f)
            
            rows = []
            with open('bedApp/static/uploads/temp', 'r') as csvfile: 
                # creating a csv reader object 
                printOut = csv.reader(csvfile)
                for line in printOut:
                    rows.append(line)
            print(printOut)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=out.bed'

            writer = csv.writer(response)
            for row in rows:
                writer.writerow(row)
                       
            return response
            #return render_to_response('index.html', {'output':output})---deprecated
    else:
        dataFile = uploaderOne()
    return render(request, 'index.html', {'form': dataFile})

def twoFiles(request):

    if request.method == 'POST':
        dataFile = uploaderTwo(request.POST, request.FILES)
        
        if dataFile.is_valid():
            task = request.POST['task']
            outOne = handle_uploaded_file_path(request.FILES['fileOne'])
            outTwo = handle_uploaded_file_path(request.FILES['fileTwo'])
            with open('bedApp/static/uploads/temp', "w+") as f:
                outputOne = subprocess.run(['bedtools', task, '-a', outOne, '-b', outTwo], stdout=f)
            
            rows = []
            with open('bedApp/static/uploads/temp', 'r') as csvfile: 
                # creating a csv reader object 
                printOut = csv.reader(csvfile)
                for line in printOut:
                    rows.append(line)
            print(printOut)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=out.bed'

            writer = csv.writer(response)
            for row in rows:
                writer.writerow(row)
                       
            return response
            #return render_to_response('index.html', {'output':output})---deprecated
    else:
        dataFile = uploaderTwo()
    return render(request, 'twoFiles.html', {'form': dataFile})



def output(request):

    if request.method == 'POST':
        dataFile = uploader(request.POST, request.FILES)

        if dataFile.is_valid():
            bedFile = request.FILES['file']
            for column in csv.reader(bedFile, delimiter='\t'):
                _, created = Table.objects.update_or_create(
                    chrome = column[1],
                    start = column[2],
                    end = column[3],
                )
            try:
                output = subprocess.check_output(Table,shell=True)
            except subprocess.CalledProcessError:
                exit_code, error_msg = output.returncode, output.output
        else:
            return HttpResponse('NOT SUCCESSFULLY UPLOADED')
            #context = {'tables': Table.objects.all()}
        return(request, 'output.html', locals())


