from django import forms

class PostForm(forms.Form):
    content = forms.CharField(max_length=200)
    created_at = forms.DateTimeField()

class RelayForm(forms.Form):
    relay = forms.CharField(max_length=200)
