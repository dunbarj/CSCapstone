"""GroupsApp Forms

Created by Naman Patwari on 10/10/2016.
"""
from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    description = forms.CharField(label='Description', max_length=300)
	
class GroupMemberForm(forms.Form):
	email = forms.CharField(label='Email', max_length=50)
	
class CommentForm(forms.Form):
	comment = forms.CharField(label='Comment', max_length=500)
    
class GroupProjectForm(forms.Form):
    group = forms.CharField(label='Group')