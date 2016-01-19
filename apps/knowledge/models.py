from django.db import models
from django.utils import timezone
from django.conf import settings

from apps.account.models import User
from apps.utils.mail import MailSender


class Quote(models.Model):
    author = models.CharField(max_length=32)
    text = models.CharField(max_length=512)

    def __unicode__(self):
        return self.author + ' - ' + self.text[:16]


class Article(models.Model):
    TAGS = ['django', 'python', 'angular', 'angularjs', 'javascript', 'web', 'mobile', 'android', 'nodejs']

    url = models.URLField(max_length=256)
    title = models.CharField(max_length=256, null=True, blank=True)
    image_url = models.URLField(max_length=256, null=True, blank=True)
    tags = models.CharField(max_length=128, null=True, blank=True)
    short_description = models.CharField(max_length=512, null=True, blank=True)
    user = models.ForeignKey(User, related_name='articles', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return str(self.url)

    def send_mail(self):
        """
        send mail to all users in the project on new feed
        """
        user = User(email="team@rawdatatech.com")
        if self.title:
            title = self.title
        else:
            title = "New Article"
        mail = MailSender(user)
        mail.compose('[Info] ' + " " + title, 'knowledge/email/article-feed', {'article': self})
        mail.send_async()
