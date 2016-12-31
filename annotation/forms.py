# -*- coding:utf-8 -*-
from django import forms
from .models import Token

# class DefaultAnnotationForm(forms.Form):
#     coda = forms.CharField(label='CODA', max_length=15,
#                            widget=forms.TextInput(attrs={'placeholder': 'CODA', 'aria-describedby': 'helpBlock_coda',
#                                                          'class': 'form-control'}))
#     segmentation = forms.CharField(label='Segmentation', max_length=15, widget=forms.TextInput(
#         attrs={'placeholder': 'Segmentation', 'aria-describedby': 'helpBlock_seg',
#                'class': 'form-control'}))
#     pos = forms.CharField(label='POS', max_length=15, widget=forms.TextInput(
#         attrs={'placeholder': 'Part-of-speech', 'aria-describedby': 'helpBlock_pos',
#                'class': 'form-control'}))
#     ambiguity = forms.BooleanField(label=u'ملتبس', initial=False, required=False)
#
#     def process_labels(self):
#         cd = self.cleaned_data
#         print cd

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['default_coda', 'default_segmentation', 'default_pos', 'ambiguous']
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }