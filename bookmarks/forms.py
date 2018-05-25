from djang import forms
from .model import Bookmark

class BookmarkForm(forms.ModelForm);

  class Meta:
    model = Bookmark
    fields = ("url", "name", "notes")