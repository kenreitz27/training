from django import forms

class MessageForm(forms.Form): 
  message = forms.CharField(
    max_length=50,
    widget=forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Message to Send",
      'autofocus': 'autofocus'
    })
  )
  