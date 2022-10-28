from django.forms import ModelForm
from .models import Essence

class EssenceForm(ModelForm):
  class Meta:
    model = Essence
    fields = ['date', 'absorbtions']
