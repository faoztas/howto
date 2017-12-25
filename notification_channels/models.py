from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.timesince import timesince
from django.utils import timezone


class Notification(models.Model):
    Type = models.CharField(max_length=255, blank=True, null=True)
    recipient = models.ForeignKey(
        User, null=False, blank=False,
        related_name="notifications", on_delete=models.CASCADE
    )
    generator = models.ForeignKey(
        User, related_name='activity_notifications',
        null=True, blank=True
    )
    target_ctype = models.ForeignKey(
        ContentType, related_name='related_notifications',
        blank=True, null=True, on_delete=models.CASCADE
    )
    target_id = models.CharField(max_length=255, blank=True, null=True,)
    target = GenericForeignKey('target_ctype', 'target_id')
    action_obj_ctype = models.ForeignKey(
        ContentType, related_name='action_notifications',
        blank=True, null=True, on_delete=models.CASCADE
    )
    action_obj_id = models.CharField(max_length=255, blank=True, null=True,)
    action_obj = GenericForeignKey('action_obj_ctype', 'action_obj_id')
    read = models.BooleanField(default=False, blank=False)
    seen = models.BooleanField(default=False, blank=False)
    action_verb = models.CharField(
        max_length=255, default="You recieved a notification."
    )
    description = models.TextField(null=True, blank=True)
    reference_url = models.CharField(
        max_length=1023, blank=True, null=True, default="#"
    )
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        timedlta = timesince(self.timestamp, timezone.now())
        fields = {
            'recipient': self.recipient,
            'generator': self.generator.username if self.generator else None,
            'action_obj': self.action_obj,
            'target': self.target,
            'action_verb': self.action_verb,
            'timesince': timedlta,
        }

        if self.generator:
            if self.action_obj:
                if self.target:
                    return '%(generator)s %(action_verb)s %(target)s %(action_obj)s %(timesince)s ago' % fields
                return '%(generator)s %(action_verb)s %(action_obj)s %(timesince)s ago' % fields
            return '%(generator)s %(action_verb)s %(timesince)s ago' % fields

        if self.action_obj:
            if self.target:
                return '%(action_verb)s %(target)s %(action_obj)s %(timesince)s ago' % fields
            return '%(action_verb)s %(action_obj)s %(timesince)s ago' % fields
            return '%(action_verb)s %(timesince)s ago' % fields

    def __unicode__(self):
        return self.__str__(self)
