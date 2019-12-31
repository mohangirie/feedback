from django import forms

class FeedbackForm(forms.Form):
    name= forms.CharField(
        label='Enter your Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name:'
            }
        )
    )
    rating= forms.IntegerField(
        label= 'Enter your rating',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your rating'
            }
        )
    )
    loc= forms.CharField(
        label= 'Enter your location',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Your location'
            }
        )
    )
    feedback= forms.CharField(
        help_text="Thanks for your valuble feedback",
        label='Enter your feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback'
            }
        )
    )
