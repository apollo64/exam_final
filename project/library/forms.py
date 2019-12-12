from django import forms

from library.models import Author


class AuthorForm(forms.ModelForm):
    image = forms.ImageField(label='Фото', required=False)
    birth_date = forms.DateField(label='Дата рождения',
                                 input_formats=['%d/%m/%Y'],
                                 required=True)
    death_date = forms.DateField(label='Дата смерти',
                                 input_formats=['%d/%m/%Y'],
                                 required=True)

    class Meta:
        model = Author
        exclude = ["status"]
        fields = ['name', 'birth_date', 'death_date', 'biography', 'image']

    def save(self):
        author = super().save()
        return author
