from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils import timezone

User = get_user_model()


class VoteQuestionQueryset(models.QuerySet):
    def active(self):
        now = timezone.now()
        return self.filter(
            Q(start_date__lte=now) &
            Q(Q(end_date__gte=now) | Q(end_date__isnull=True)))


class VoteQuestion(models.Model):
    SINGLE = 's'
    MULTIPLE = 'm'
    TEXT = 't'

    TYPE_CHOICE = (
        (SINGLE, 'Одиночный выбор'),
        (MULTIPLE, 'Множественный выбор'),
        (TEXT, 'Текстовый выбор'),
    )
    title = models.CharField(max_length=32, verbose_name='Заголовок')
    description = models.CharField(max_length=128, verbose_name='Описание', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Создан в', auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания', blank=True, null=True)
    v_type = models.CharField(verbose_name='Тип варианта', choices=TYPE_CHOICE, default=SINGLE, max_length=1)
    objects = VoteQuestionQueryset.as_manager()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    @property
    def is_active(self):
        now = timezone.now()
        if self.end_date and self.start_date < now < self.end_date:
            return True
        elif not self.end_date and self.start_date < now:
            return True
        return False


class VoteVariant(models.Model):
    question = models.ForeignKey(VoteQuestion, related_name='variants', on_delete=models.CASCADE)
    description = models.CharField(max_length=128, verbose_name='Текст', blank=True, null=True)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class VoteAnswer(models.Model):
    user = models.ForeignKey(User, related_name='my_answers', null=True, on_delete=models.SET_NULL, )
    question = models.ForeignKey(VoteQuestion, related_name='answers', on_delete=models.CASCADE)
    variants = models.ManyToManyField(VoteVariant, related_name='answers', blank=True, null=True)

    value = models.TextField(verbose_name='Строковое значение', max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата ответа', auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответ пользователей'
        ordering = ['-created_at']
