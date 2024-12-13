from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.
def create_movie_review(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('home')
    else:
        form = MovieForm()
        context = {
            "form": form,
        }
        return render(request, 'reviews/create_movie_review.html', context)