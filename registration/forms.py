from django import forms

class SignupForm(forms.Form):
    username = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    #integrants = forms.CharField(widget=forms.Textarea(attrs={'rows:1', 'cols':60}))
    integrants = forms.CharField()
    organization = forms.CharField()

    def passwwd_confirmation(self):
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match!")
        return message
