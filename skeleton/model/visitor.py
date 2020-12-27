from tortoise.models import Model
from tortoise import fields


class Visitor(Model):
    class Meta:
        table = 'visitor'

    id = fields.IntField(pk=True)
    account = fields.CharField(100)
    password = fields.CharField(100)
    nickname = fields.CharField(200)
    create_at = fields.DatetimeField()
