from django import forms

from items.models import Category, Item


# class ItemCreationForm(forms.Form):
#     name = forms.CharField(max_length=70)
#     description = forms.CharField(widget=forms.Textarea(
#         attrs={'rows': 2}
#     ))
#     price = forms.IntegerField()
#     count = forms.IntegerField()
#     # category_id = forms.ChoiceField(
#     #     choices=((1, 'Первый'), (2, 'Второй')))
#     category_id = forms.ModelChoiceField(
#         queryset=Category.objects.all()
#     )

class ItemCreationForm(forms.ModelForm):




    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'count', 'category']
