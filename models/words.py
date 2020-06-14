# /usr/bin/env python3.8
# -*- coding: utf-8 -*-
import datetime
from peewee import PrimaryKeyField, ForeignKeyField, DateTimeField, TextField
from lib.DataBase import BaseModel


class Words(BaseModel):
    id = PrimaryKeyField(null=False)
    word = TextField(null=False, default='')

    class Meta:
        db_table = "words"
        order_by = ('id',)



