import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from app.models import Tag, Question, Profile, Answer, Like, QuestionLike, AnswerLike


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("ratio", nargs="+", type=int)

    def handle(self, *args, **options):
        ratio = options['ratio'][0]
        tags = [Tag(name=f'Тэг {i}') for i in range(ratio)]
        Tag.objects.bulk_create(tags)
        users = [User(username=f'user {i}', password="eebniovnbenwobn") for i in range(ratio)]
        User.objects.bulk_create(users)
        profiles = [Profile(user=users[i]) for i in range(ratio)]
        Profile.objects.bulk_create(profiles)
        questions = [
            Question(title=f'title {i}', author=profiles[random.randint(0, ratio - 1)],
                     text=f'question text of question {i}') for
            i in range(ratio * 10)]
        Question.objects.bulk_create(questions, batch_size=ratio)
        for question in questions:
            question.tags.add(tags[random.randint(0, ratio - 1)])
        answers = [
            Answer(author=profiles[random.randint(0, ratio - 1)], question=questions[random.randint(0, ratio * 10 - 1)],
                   text=f'answer {i} for question ') for
            i in range(ratio * 100)]
        Answer.objects.bulk_create(answers, batch_size=ratio)
        likes = [Like(user=profiles[random.randint(0, ratio - 1)]) for i in range(ratio * 200)]
        Like.objects.bulk_create(likes, batch_size=ratio)
        answerLikes = [0] * 150 * ratio
        questionLikes = [0] * 50 * ratio
        ind = 0
        for like in Like.objects.all():
            if ind < 150 * ratio:
                answerLikes[ind] = AnswerLike(answer=answers[random.randint(0, ratio * 100 - 1)], like=like)
            else:
                questionLikes[ind - 150 * ratio] = QuestionLike(question=questions[random.randint(0, ratio * 10 - 1)],
                                                                like=like)
            ind += 1

        QuestionLike.objects.bulk_create(questionLikes,batch_size=ratio)
        AnswerLike.objects.bulk_create(answerLikes, batch_size=ratio)
