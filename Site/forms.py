from django import forms
from .models import Guest


class GuestForm(forms.ModelForm):
    presence = forms.ChoiceField(
        choices=Guest.PRESENCE_CHOICES,
        widget=forms.RadioSelect,
    )
    plusone = forms.ChoiceField(
        choices=Guest.PLUS_ONE_CHOICES,
        widget=forms.RadioSelect,
        required=False,
    )

    class Meta:
        model = Guest
        fields = ['name', 'presence', 'plusone', 'drink']
        widgets = {
            'presence': forms.RadioSelect,
            'plusone': forms.RadioSelect,
            'drink': forms.Textarea(attrs={'rows': 4, 'style': 'width: 100%; padding: 8px;'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        presence = cleaned_data.get('presence')
        plusone = cleaned_data.get('plusone')

        # Если гость придет
        if presence == 'yes' and not plusone:
            self.add_error('plusone', 'Пожалуйста, укажите, придете ли Вы с парой.')

        # Если гость не придет
        if presence == 'no':
            cleaned_data['plusone'] = 'no'
            cleaned_data['drink'] = ''

            if 'plusone' in self._errors:
                del self._errors['plusone']
            if 'drink' in self._errors:
                del self._errors['drink']

        return cleaned_data
