from app.models import Rasmlar
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class RsamForm(forms.ModelForm):
    class Meta:
        model=Rasmlar
        fields=("image",)
        widgets={"addres":forms.widgets.FileInput(attrs={"class":"form-control unicase-form-control text-input"})
        }
    # def clean_login(self):
    #     login=self.cleaned_data["login"]
    #     if User.objects.filter(username=login).exists():
    #         raise ValidationError("Bu login band!")
    #     elif len(login)<=3 or len(login)>=20:
    #         raise ValidationError("Parolni 3 ta belgidan ko`p 20 tadan kam quying!")
    #     return login
    # def clean_phone(self):
    #     phone=self.cleaned_data["phone"]
    #     if len(phone)!=13 or not phone[1:].isdigit() or phone[0]!='+':
    #         raise ValidationError("Namunaga qarab telefon raqamni kiriting!")
    #     return phone

    # def clean_card_nomer(self):
    #     card_nomer=self.cleaned_data["card_nomer"]
    #     if len(card_nomer)!=16 or not card_nomer.isdigit():
    #         raise ValidationError("Namunaga qarab karta raqamni kiriting!")
    #     return card_nomer




    # def cleand_password1(self):
    #     super().clean()
    #     password1=self.cleaned_data["password1"]
    #     if password1:
    #         password_validation.validate_password(password1)
    #     return password1
    #
    # def clean_password2(self):
    #     super().clean()
    #     p1=self.cleaned_data["password1"]
    #     p2=self.cleaned_data["password2"]
    #     if p1 and p2 and p1 != p2:
    #         raise ValidationError("Parollar mos emas!")
    #     return p2
    # def save(self, commit=True):
    #     user= super().save(commit=False)
    #
    #     login=self.cleaned_data["login"]
    #     password1=self.cleaned_data["password1"]
    #     u=User.objects.create_user(username=login,password=password1)
    #     user.user=u
    #     if commit:
    #         user.save()
    #     return user