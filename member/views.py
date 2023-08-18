from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from .models import Member

def login(request):
    if request.method == 'POST':
        entered_last_four = request.POST.get('phone_last_four', '')
        try:
            member = Member.objects.get(phone_last_four=entered_last_four)
            main_url = reverse('member:main', args=[entered_last_four])
            return redirect(main_url)
        except ObjectDoesNotExist:
            error_message = "입력한 전화번호와 일치하는 회원 정보가 없습니다."
            return render(request, 'member/login.html', {'error_message': error_message})

    return render(request, 'member/login.html')

def main(request, phone_last_four):
    try:
        member = Member.objects.get(phone_last_four=phone_last_four)
        points = member.point
    except Member.DoesNotExist:
        points = 0

    return render(request, 'main/main.html', {'points': points})
