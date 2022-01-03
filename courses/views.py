from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *
import mimetypes
import os
from django.http.response import HttpResponse
from applications.forms import ApplicationForm

# def download_pdf_file(request, filename=''):
#     if filename != '':
#         # Define Django project base directory
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + '/uploads/learnership_brochures/' + filename
#         # Open the file for reading content
#         # filename = 'Sisekelo-Brouchure-End-User.pdf'
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'index.html')


def index(request):
    qs = Learnership.objects.all()
    #image = Learnership.objects.get(image)
    jobs = Learnership.objects.all().count()
    # #user = User.objects.all().count()
    company_name = Learnership.objects.all()
    paginator = Paginator(qs, 5)  # Show 5 courses per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': jobs,
        'company_name': company_name,
        #'image' = image
        #'candidates': user
    }
    return render(request, "index.html", context)





def post_new(request):
    form = ApplicationForm()
    return render(request, 'index.html', {'form': form})