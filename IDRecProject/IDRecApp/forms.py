from django import forms


class IDPhotoForm(forms.Form):
    filename = forms.FileField(max_length=200, widget=(forms.FileInput(attrs={'class': 'form-control input-file'})))


class IDDataForm(forms.Form):
    forenames = forms.CharField(max_length=200, widget=(forms.TextInput(attrs={'class': 'form-control'})))
    surname = forms.CharField(max_length=200, widget=(forms.TextInput(attrs={'class': 'form-control'})))
    date_of_birth = forms.DateField(widget=(forms.DateInput(attrs={'class': 'form-control'})))
    country_of_birth = forms.CharField(max_length=200, widget=(forms.TextInput(attrs={'class': 'form-control'})))
    date_issued = forms.DateField(widget=(forms.DateInput(attrs={'class': 'form-control'})))
    id_no = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control'})))