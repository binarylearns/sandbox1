from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import StudentProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=150, required=True)
    student_class = forms.ChoiceField(choices=StudentProfile.CLASS_CHOICES)
    section = forms.CharField(max_length=20, required=False)
    school = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply minimal underline styling to every field
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full border-0 border-b border-gray-300 bg-transparent '
                         'py-2 text-sm text-black focus:outline-none '
                         'focus:border-black transition-colors',
            })