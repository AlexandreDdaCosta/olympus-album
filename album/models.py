from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _


class Media(models.Model):
    description = models.CharField(max_length=255,
                                   null=True)
    create_date = models.DateTimeField(_('Created'),
                                       null=True)
    url_path = models.URLField(max_length=200,
                               null=False,
                               unique=True)

    def __unicode__(self):
        return u'%s' % (self.url_path)


class Subject(models.Model):
    name = models.CharField(db_index=True,
                            max_length=100,
                            null=False,
                            unique=True)
    description = models.CharField(max_length=255)
    media = models.ForeignKey(Media,
                              null=True,
                              on_delete=models.CASCADE)
    order = models.IntegerField(MinValueValidator(1),
                                null=False,
                                unique=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Effect(models.Model):
    name = models.CharField(db_index=True,
                            max_length=100,
                            null=False,
                            unique=True)
    description = models.CharField(max_length=255,
                                   null=False)

    def __unicode__(self):
        return u'%s' % (self.name)


class Album(models.Model):
    title = models.CharField(db_index=True,
                             max_length=255,
                             null=False)
    description = models.TextField(null=False)
    media = models.ForeignKey(Media,
                              null=False,
                              on_delete=models.CASCADE)
    opening_text = models.TextField(null=True)
    opening_effect = models.ForeignKey(Effect,
                                       null=True,
                                       on_delete=models.CASCADE,
                                       related_name='album_opening_effect')
    closing_text = models.TextField(null=True)
    closing_effect = models.ForeignKey(Effect,
                                       null=True,
                                       on_delete=models.CASCADE,
                                       related_name='album_closing_effect')

    def __unicode__(self):
        return u'%s' % (self.title)


class AlbumEntry(models.Model):
    caption = models.TextField(null=True)
    album = models.ForeignKey(Album,
                              null=False,
                              on_delete=models.CASCADE)
    media = models.ForeignKey(Media,
                              null=False,
                              on_delete=models.CASCADE)
    order = models.IntegerField(MinValueValidator(1),
                                null=False)
    opening_effect = models.ForeignKey(
        Effect,
        null=True,
        on_delete=models.CASCADE,
        related_name='album_entry_opening_effect')
    closing_effect = models.ForeignKey(
        Effect,
        null=True,
        on_delete=models.CASCADE,
        related_name='album_entry_closing_effect')

    class Meta:
        unique_together = ('album', 'order')


class SubjectAlbum(models.Model):

    subject = models.ForeignKey(Subject,
                                null=False,
                                on_delete=models.CASCADE)
    album = models.ForeignKey(Album,
                              null=False,
                              on_delete=models.CASCADE)
    media = models.ForeignKey(Media,
                              null=False,
                              on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'album')


class SubjectAlbumOrder(models.Model):

    subject_album = models.ForeignKey(SubjectAlbum,
                                      null=False,
                                      on_delete=models.CASCADE)
    order = models.IntegerField(MinValueValidator(1),
                                null=False)

    class Meta:
        unique_together = ('subject_album', 'order')
