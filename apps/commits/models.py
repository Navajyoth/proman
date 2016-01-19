from django.db import models


class Commit(models.Model):
    url = models.URLField(max_length=512, null=True, blank=True)
    username = models.CharField(max_length=512, null=True, blank=True)
    date = models.DateTimeField()
    comment = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = "Commit"
        verbose_name_plural = "Commits"

    def __unicode__(self):
        return self.username
