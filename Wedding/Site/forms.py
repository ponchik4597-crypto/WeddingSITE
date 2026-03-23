from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):
    presence = forms.ChoiceField(
        choices=Guest.PRESENCE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )
    plusone = forms.ChoiceField(
        choices=Guest.PLUS_ONE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )

    class Meta:
        model = Guest
        fields = ['name', 'presence', 'plusone', 'drink']
        widgets = {
            'presence': forms.RadioSelect,
            'plusone': forms.RadioSelect,
            'drink': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 8px;'}),
        }
