from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo"
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
    )

    public_options = [
        ('',['Seleccione.']),
        (1,['SI']),
        (2,['NO'])
    ]
    public = forms.TypedChoiceField(
        label = "Publico",
        choices = public_options
    )