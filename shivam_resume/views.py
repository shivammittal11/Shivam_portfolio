import csv
import datetime

import pytz
from django.http import HttpResponse
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


# def get_data(request):
#     # dummy api for reports
#     print('pppppppppppppppp')
#     data = request.GET.dict()
#
#     to_date = data.get('to_date')
#     from_date = data.get('from_date')
#     report_type = data.get('type')
#     case_data = []
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="{0}"'.format('abc.csv')
#     writer = csv.writer(response)
#     if report_type == 'ambulance':
#         booking_queryset = ProjectData.objects.filter()
#         for project_obj in booking_queryset:
#             project_data = {}
#             project_data[project_obj.name] = ''
#             project_data[project_obj.description] = ''
#             case_data.append(project_data)
#         for index, data in enumerate(case_data):
#             if index == 0:
#                 # data = [x.upper() for x in data]
#                 if report_type == 'ambulance':
#                     data = ['Sl.No', 'Case ID', 'Booking Date', 'Fleet Owner', 'Executive Name',
#                             'Executive Mobile Number','Ambulance Type', 'Ambulance Number', 'Case Status',
#                             'Total Waiting Time(In Minutes)', 'Total Waiting Amount', 'Total KMs Run',
#                             'Vendor Amount', ' Total Vendor Amount', 'iRelief Amount', 'Total Tax',
#                             'Total iRelief Amount', 'Grand Total', 'Amount Paid', 'Status', 'Payment Mode']
#                 if report_type == 'bloodbank':
#                     data = ['Sl.No', 'Case ID', 'Booking Date', 'Blood Bank Executive Name',
#                             'Executive Mobile Number', 'Blood Group', 'Blood Component(s)', 'Total Units',
#                             'Cost Per Unit', 'Other Charges(If  Any)', 'Vendor Amount', 'iRelief Amount',
#                             'Per Unit iRelief Cost''Total Tax', 'Total iRelief Amount', 'Exemption Case',
#                             'Exemption Category', 'Total Amount to be Collected', 'Case Status', 'Amount Paid',
#                             'Status', 'Payment Mode']
#             writer.writerow(data)
#
#     return response


# def some_text(request):
#     project_list = []
#     skill_list = SkillData.objects.all()
#     # # # from_date = '30-11-2018'
#     from_date = datetime.datetime.strptime('29-11-2018', "%d-%m-%Y").replace(tzinfo=pytz.utc)
#     to_date = datetime.datetime.strptime('01-12-2018', "%d-%m-%Y").replace(tzinfo=pytz.utc)
#     print(from_date)
#     print(to_date)
#
#     # pst = pytz.timezone('America/Los_Angeles')
#     # from_date = pst.localize(datetime.datetime.strptime('29-11-2018', "%d-%m-%Y"))
#     # to_date = pst.localize(datetime.datetime.strptime('01-12-2018', "%d-%m-%Y"))
#     # print(from_date)
#     # print(to_date)
#     #
#     # print(from_date)
#
#     # print(to_date)
#     # # to_date = '30-11-2018'
#     # # to_date = datetime.date(to_date)
#     # datetime.datetime.utcnow().replace(tzinfo=utc)
#
#     project_queryset = ProjectData.objects.filter(created__range=[from_date, to_date])
#     user_obj = UserData.objects.get(id=1)
#     user_image = user_obj.image
#     user_image = request.scheme + '://' + request.get_host() + '/media/' + str(user_image)
#     for project_obj in project_queryset:
#         project_data = {}
#         print(project_obj.created)
#         cover_image = str(project_obj.cover_image)
#         cover_image = request.scheme + '://' + request.get_host() + '/media/' + cover_image
#         project_data[keys.KEY_PROJECT_NAME] = project_obj.name
#         project_data[keys.KEY_PROJECT_TITLE] = project_obj.title
#         project_data[keys.KEY_PROJECT_COVER_IMAGE] = cover_image
#         project_data[keys.KEY_PROJECT_STATUS] = project_obj.status
#         project_data[keys.KEY_PROJECT_DESCRIPTION] = project_obj.description
#         project_data[keys.KEY_PROJECT_POSITION] = project_obj.position
#         project_data['created'] = project_obj.created
#         project_data['time'] = str(datetime.datetime.now())
#         if project_obj.position % 2 == 0:
#             project_data[keys.KEY_ODD] = True
#         else:
#             project_data[keys.KEY_ODD] = False
#         project_list.append(project_data)
#
#         project_list = sorted(project_list, key=lambda x: x['project_position'])
#     return JsonResponse({'success': True, 'project_list': project_list})
