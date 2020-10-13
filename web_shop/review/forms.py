from django import forms
from django.contrib.auth.models import User
from . models import CustomerReview


CHOICES=[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)]
class CustomerReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=CHOICES,
             widget=forms.RadioSelect(attrs={"required": True}),
             required=True)

    class Meta:
        model = CustomerReview
        fields = ('rating', 'author', 'comment')
