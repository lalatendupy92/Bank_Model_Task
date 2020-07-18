from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView, View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class User_login_page(View):
    def get(self,request):
        return render(request,'index.html')


class User_details_data(View):
    def get(self,request):
        account = Account_type.objects.all()
        return render(request,'User_details_fill_form.html',{'user_form':User_Details_Fill(), 'account': account})
    def post(self,request):
        if request.method == 'POST':
            uf=User_Details_Fill(request.POST , request.FILES)
            if uf.is_valid():
                db=uf.save(commit=False)
                db.user_status = 'pending'
                db.save()
                messages.success(request,'Request Send..')
                return redirect('User_login_page')
            else:
                messages.error(request,'Invalid Data')
                return redirect('User_login_page')


class Admin_Page(View):
    def get(self,request):
        user_data=User_Details.objects.all()
        return render(request,'admin_page.html',{"user_data":user_data})


def pending_status(request):
    pending_status = User_Details.objects.filter(user_status='pending')
    return render(request,'status_check.html',{'status_check':pending_status})


def approve_status(request):
    u_id=request.GET.get('uid')
    user_obj=User_Details.objects.filter(user_id=u_id)
    user_obj.update(user_status='approved')
    send_mail(
        'Account Status.',
        'Congrats..Your Account status is approved.',
        settings.EMAIL_HOST_USER,
        [user_obj[0].user_email, ]
    )
    return render(request,'status_check.html',{"messeage":"Request approved."})


def reject_status(request):
    u_id = request.GET.get('uid')
    user_obj = User_Details.objects.filter(user_id=u_id)
    user_obj.update(user_status='rejected')
    send_mail(
        'Account Status.',
        'Your Account is Rejected.',
        settings.EMAIL_HOST_USER,
        [user_obj[0].user_email,]
    )
    return redirect('pending_status')