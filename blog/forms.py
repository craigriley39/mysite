from .models import Entry,Category

from django import forms

class EntryModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder' : 'Enter your text here'}))
    #slug = forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Slug is autogenerated if left blank'}))
    #slug = forms.CharField(required=True)
    class Meta:
        model = Entry


        fields = ['title','body','image','category','created_by']
