from django.shortcuts import render,redirect
from  django.http import HttpResponse
from .forms import IDPhotoForm,IDDataForm
from .models import *
import os
import sys
import json
import string
import subprocess
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath(__file__)))


def home(request):

    id_photo_form = IDPhotoForm()

    context = {'id_photo_form': id_photo_form}

    if request.method == 'POST' and request.FILES['filename']:

        id_photo_form = IDPhotoForm(request.POST,request.FILES)

        print(id_photo_form.errors)

        if id_photo_form.is_valid():

            file_path = request.FILES['filename']

            image_name = file_path.name

            image_name = str(image_name)

            if image_name.endswith(".jpg") or image_name.endswith(".png") or image_name.endswith(".jpeg"):

                import random

                digits = string.digits

                user_id = 'AID'.join((random.choice(digits) for i in range(5)))

                # letters_and_digits = string.ascii_letters + string.digits
                #
                # result_str = ''.join((random.choice(letters_and_digits) for i in range(10)))
                #
                # file_name_modified = str(file_path).split('.')[-2]+str(result_str)+'.jpg'
                #
                # file_path_uploaded = os.path.join(BASE_DIR,'./filepaths/'+image_name)

                new_file = ImageModel(filepaths=file_path, filename=image_name, user_id=user_id)

                new_file.save()

                os.system('python3 ./IDRecApp/prediction.py ./IDRecApp/static/filepaths/'+str(image_name))

                f = open("./IDRecApp/json_files/{}.json".format(str(image_name).split('.')[-2]))

                data_dict = json.load(f)

                return render(request, 'pages/register.html', context={'data_dict':data_dict,'image_path':{'file_path':'/static/filepaths/'+str(image_name)}})


            else:

                id_photo_form = IDPhotoForm()

                format_message="Unsupported image format, supported formats are .png, .jpeg and .jpg ";

                return render(request,'pages/home.html',{'fmsg':format_message,'id_photo_form':id_photo_form})

        else:
            return render(request,template_name="pages/home.html",context=context)

    return render(request,template_name="pages/home.html",context=context)


def register(request):

    id_photo_form = IDPhotoForm()

    if request.method == 'POST':

        registerform = IDDataForm(request.POST)

        if registerform.is_valid():

            registerform = IDDataForm(request.POST)

            id_no = request.POST['id_no']
            surname = request.POST['surname']
            forenames = request.POST['forenames']
            country_of_birth = request.POST['country_of_birth']
            date_of_birth = request.POST['date_of_bitrh']
            date_issued = request.POST['date_issued']

            if id_no == '' or surname =='' or forenames == '' or country_of_birth == '' or date_of_birth == '' or date_issued == '':

                nullerror = "Complete filling information"

                context = {'registerform': registerform,'merror':nullerror}

                return render(request,'pages/register.html',context)
            else:
                new_data = DataModel(user_id='',surname=surname,forenames=forenames, country_of_birth=country_of_birth,
                                     id_no=id_no, date_issued=date_issued, date_of_birth=date_of_birth)
                new_data.save()

                return redirect('home')

    else:

       return render(request,'pages/home.html',{'id_photo_form':id_photo_form})

    return render(request,'pages/home.html',{'id_photo_form':id_photo_form})