from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


# Create your models here.
class QuestionManager(models.Manager):
    def get_new(self):
        return self.all().order_by('created_at').reverse()

    def get_hot(self):
        return self.all().annotate(like_count=Count('likes')).order_by('like_count').reverse()

    def get_one_question(self, question_id):
        return self.all().filter(id=question_id)[0]

    def get_with_tag(self, tag_name):
        return self.all().filter(tags__name=tag_name)


class AnswerManager(models.Manager):
    def get_answers(self, question):
        return self.all().filter(question=question)

    def get_answers_count(self, question):
        return self.all().filter(question=question).count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=35)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=85)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(Like, through="QuestionLike")
    created_at = models.DateField(auto_now_add=True)

    objects = QuestionManager()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Like, through="AnswerLike")
    text = models.CharField(max_length=1000)

    objects = AnswerManager()


class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'like')


class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    like = models.ForeignKey(Like, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('answer', 'like')
