from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Escribe el Titulo'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'Titulo no valido, es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$','Titulo no valido, contiene simbolos extraños','invalid_title')
        ]
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators=[
            validators.MaxLengthValidator(60,'Solo puedes escribir 20 caracteres como Máximo')
        ]
    )

    content.widget.attrs.update({
        'placeholder': 'Escribe el Contenido',
        'class': 'contenido_form_article',
        'id': 'id_content'
    })

    public_options = [
        (1,'SI'),
        (2,'NO')
    ]
    public = forms.TypedChoiceField(
        label = "Publico",
        choices = public_options
    )