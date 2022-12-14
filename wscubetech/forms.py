from django.forms import forms

#class usersforms(forms.frrm):
#    num1=forms.forms.CharField(lavel="Value 1", required=False,width=forms.TextInput(attrs={'class':"form-control"}))
#    num2=forms.forms.CharField(lavel="Value 2", width=forms.TextInput(attrs={'class':"form-control"}))

class usersform(forms.Form):
    #num1=forms.CharField(label="value 1",widget=forms.Textarea(attrs={'class':"form-control"}))
    #num2=forms.CharField(label="value 2",required="False",widget=forms.Textarea(attrs={'class':"form-control"}))
    class Meta:
        fields='__all__'