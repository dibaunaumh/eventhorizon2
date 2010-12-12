from django.db import models

class Text(models.Model):
    text = models.CharField(_('text'), max_length=10000, help_text=_('document text'))

    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('text')

    def __unicode__(self):
        return self.text

class Document(models.Model):
    discussion_id = models.IntegerField()
    keywords = models.CharField(_('keywords'), max_length=1000, help_text=_('document keywords'))

    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')

    def __unicode__(self):
        return self.discussion_name

class Term(models.Model):
    num_docs = models.IntegerField(default=0)
    term = models.CharField(_('term'), max_length=50, help_text=_('term'))

    class Meta:
        verbose_name = _('term')
        verbose_name_plural = _('terms')

    def __unicode__(self):
        return self.term


class Document_Term(models.Model):
    document_id = models.IntegerField()
    term_id = models.IntegerField()
    tf = models.FloatField()
