from django import forms
from .models import MovieReview

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'featured_image', 'rating', 'review_text', 'release_date', 'runtime', 'director']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }