from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList
from .models import Client

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])
        
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields =["prenom","nom","email","tel"]
        widget = {
            'prenom': TextInput(attrs={'class': 'form-control'}),
            'nom': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'tel': TextInput(attrs={'class': 'form-control'})
        }
