from django import forms

class SurveyForm(forms.Form):
    description = forms.CharField(
        label="Your Description",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Example: I enjoy spending time alone reading, but I also like to go out with friends occasionally.",
                "rows": 6,  
            }
        )
    )
