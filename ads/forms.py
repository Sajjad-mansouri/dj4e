from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Ad,Comment
from .humanize import naturalsize


class AdForm(forms.ModelForm):
	max_upload_limit = 2 * 1024 * 1024
	max_upload_limit_text = naturalsize(max_upload_limit)
	picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
	upload_field_name = 'picture'
	class Meta:
		model=Ad
		fields=['title','price','text','picture']

	def clean_picture(self):
		pic = self.cleaned_data.get('picture')
		if pic is None:
			return
		if len(pic)>self.max_upload_limit:
			self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")
		return pic
	def save(self,commit=True):
		instance=super().save(commit=False)
		pic=instance.picture
		if isinstance(pic,InMemoryUploadedFile):
			print('**isinstance**')
			byte_arr=pic.read()
			instance.content_type=pic.content_type
			instance.picture=byte_arr
		if commit:
			instance.save()

		return instance


class CommentForm(forms.Form):
	comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
