from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import StudentProfile


# =========================
# AUTH
# =========================

def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        StudentProfile.objects.create(
            user=user,
            full_name=form.cleaned_data['full_name'],
            student_class=form.cleaned_data['student_class'],
            section=form.cleaned_data.get('section', ''),
            school=form.cleaned_data.get('school', ''),
        )
        login(request, user)
        return redirect('profile')

    return render(request, 'accounts/register.html', {'form': form})


# =========================
# PROFILE
# =========================

@login_required
def profile(request):
    student_profile = getattr(request.user, 'student_profile', None)
    return render(request, 'accounts/profile.html', {
        'student_profile': student_profile,
    })


# =========================
# PLACEHOLDER PAGES
# (referenced in urls.py — safe to keep for now)
# =========================

@login_required
def classes(request):
    return render(request, 'accounts/classes.html')


@login_required
def lp(request):
    return render(request, 'accounts/lab_practical.html')


@login_required
def f1st(request):
    return render(request, 'accounts/1st.html')

@login_required
def lp(request):
    student_profile = getattr(request.user, 'student_profile', None)
    return render(request, 'accounts/lab_practical.html', {
        'student_profile': student_profile,
    })


def english_typing(request):
    return render(request, "accounts/subtopics/english_typing.html")