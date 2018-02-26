from django import forms

class user_add(forms.Form):
    item = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-dark', 'placeholder': 'Add To List:'}))