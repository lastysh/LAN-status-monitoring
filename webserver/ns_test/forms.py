from django import forms
# from captcha.fields import CaptchaField


class Commentinput(forms.Form):
    comment = forms.CharField(label='备注', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
