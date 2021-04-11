from django import forms
from .models import *


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ("name", "email", "message")


####################
# Textare : form-control mb-10
# inputs:  common-input mb-20 form-control
####################
