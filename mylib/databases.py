# -*- coding: utf-8 -*-
from peewee import *

# database = MySQLDatabase('MYX', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost',
# 'user': 'MYX', 'password': '123456'})

database = SqliteDatabase('../myDatabase.db')


class KeyWords(Model):
    site = CharField(max_length=255)
    url = CharField(max_length=255)

    class Meta:
        table_name = 'url_cache'
        database = database


class BaiDuAccountCookies(Model):
    account = CharField(max_length=255)
    password = CharField(max_length=255)
    email = CharField(max_length=255)
    cookie = TextField()

    class Meta:
        table_name = 'baidu_account_cookies'
        database = database
