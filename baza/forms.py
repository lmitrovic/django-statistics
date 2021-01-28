from django.forms import ModelForm, Form
import django.forms as f
from .models import Mobile, Comment
from django import forms


class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = ['producer', 'model', 'price']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'username', 'mobile'] 

class ProducerForm(ModelForm):
    class Meta:
        model = Mobile
        fields = ['producer'] 


                      