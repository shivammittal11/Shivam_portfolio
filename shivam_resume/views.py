from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import keys
import time
from shivam_resume.models import SkillData, ProjectData, UserData, ContactUs


def timestamp():
    ts = time.time()
    return ts


def home_page(request):
    project_list = []
    skill_list = SkillData.objects.all()
    project_queryset = ProjectData.objects.all()
    user_obj = UserData.objects.get(id=1)
    user_image = user_obj.image
    user_image = request.scheme + '://' + request.get_host() + '/media/' + str(user_image)
    for project_obj in project_queryset:
        project_data = {}
        cover_image = str(project_obj.cover_image)
        cover_image = request.scheme + '://' + request.get_host() + '/media/' + cover_image
        project_data[keys.KEY_PROJECT_NAME] = project_obj.name
        project_data[keys.KEY_PROJECT_TITLE] = project_obj.title
        project_data[keys.KEY_PROJECT_COVER_IMAGE] = cover_image
        project_data[keys.KEY_PROJECT_STATUS] = project_obj.status
        project_data[keys.KEY_PROJECT_DESCRIPTION] = project_obj.description
        project_data[keys.KEY_PROJECT_POSITION] = project_obj.position
        if project_obj.position % 2 == 0:
            project_data[keys.KEY_ODD] = True
        else:
            project_data[keys.KEY_ODD] = False
        project_list.append(project_data)

        project_list = sorted(project_list, key=lambda x: x['project_position'])
    return render(request, 'index.html', {keys.KEY_SKILLS_LIST: skill_list,
                                         keys.KEY_PROJECT_LIST: project_list,
                                         keys.KEY_USER_IMAGE: user_image,
                                        keys.KEY_TIMESTAMP: timestamp()})


@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get(keys.KEY_NAME)
        email = request.POST.get(keys.KEY_EMAIL)
        contact_no = request.POST.get(keys.KEY_CONTACT_NO)
        message = request.POST.get(keys.KEY_MESSAGE)

        ContactUs.objects.create(name=name, email=email, contact_no=contact_no, message=message)
        message1 = 'Your Details has been Sent Successfully'
        return JsonResponse({keys.KEY_SUCCESS: True, keys.KEY_MESSAGE:message1})
    else:
        message1 = 'Please Try Again'
        return JsonResponse({keys.KEY_SUCCESS: False, keys.KEY_MESSAGE: message1})

