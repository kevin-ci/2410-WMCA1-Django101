from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def film_category():
        return Category.objects.get(name="Film")

    @staticmethod
    def tv_category():
        return Category.objects.get(name="TV Series")

    @staticmethod
    def game_category():
        return Category.objects.get(name="Video Game")


class CommonReviewData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    review_text = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} reviewed by {self.user}"


class MovieReview(CommonReviewData):
    runtime = models.DurationField()
    director = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.film_category)

class TVReview(CommonReviewData):
    number_of_episodes = models.IntegerField()
    showrunner = models.CharField(max_length=100)
    average_episode_length = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.tv_category)

class GameReview(CommonReviewData):
    studio = models.CharField(max_length=100)
    time_to_beat = models.DurationField()
    number_of_players = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=Category.game_category)