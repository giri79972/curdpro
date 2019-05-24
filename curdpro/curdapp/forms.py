from django import forms
class ProductForm(forms.Form):
    fproduct_id=forms.IntegerField(label='Enter Your Product Id',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Product Id'}))
    fproduct_name=forms.CharField(label='Enter Your Product Name',widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Product Name'}))
    fproduct_cost=forms.IntegerField(label='Enter Your Product Cost',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Product Cost'}))
    fproduct_color=forms.CharField(label='Enter Your Product Color',widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Product Color'}))
    fproduct_class=forms.CharField(label="Enter Your Product Class",widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Product Class'}))
    fnumber_of_products=forms.IntegerField(label="Enter Number of Products",widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Number of Products'}))
    fcustomer_name=forms.CharField(label="Enter Customer Name",widget=forms.TextInput(attrs={'class':'form_control','placeholder':'Customer Name'}))
    fmobile_number=forms.IntegerField(label="Enter Mobile Number",widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Mobile Number'}))
    femail=forms.EmailField(label="Enter Customer EmailID",widget=forms.EmailInput(attrs={'class':'form_control','placeholder':'Email ID'}))

class UpdateForm(forms.Form):
    ufproduct_id=forms.IntegerField(label='Enter Your Product Id',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Product Id'}))
    ufproduct_cost=forms.IntegerField(label='Enter Your Product Cost',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Product Cost'}))

class DeleteForm(forms.Form):
    dfproduct_id=forms.IntegerField(label='Enter Your Product Id',widget=forms.NumberInput(attrs={'class':'form_control','placeholder':'Product Id'}))