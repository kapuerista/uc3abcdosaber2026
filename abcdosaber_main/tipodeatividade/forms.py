from django import forms

class TiposdeAtividadeForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe a descrição do Título'
    )
    
class TiposdeAtividadeAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text='Informe o código do Título')
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe a descrição do Título'
    )