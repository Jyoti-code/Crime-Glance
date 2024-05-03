from django.shortcuts import render
from otp import settings
from django.http import JsonResponse
# from rest_framework.response import Response
import json
from django.core.mail import send_mail
import os
import math
import random
import smtplib

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def predictor(request):
    if request.method == 'POST':
        emailid = json.loads(request.body)['emailid']
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        msg= otp
        email_from = settings.EMAIL_HOST_USER

        send_mail("OTP for Login ",msg,email_from,[emailid])
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # s.starttls()
        # s.login("crimeglance34@gmail.com","CrimeGlance@123" )
        # #emailid = input("Enter your email: ")
        # s.sendmail('&&&&&&&&&&&',emailid,msg)
        # a = input("Enter Your OTP >>: ")
        # if a == OTP:
        #     print("Verified")
        # else:
        #     print("Please Check your OTP again")
    
        return JsonResponse({'result':otp})
        
    return JsonResponse({'result':'send post request'})   

