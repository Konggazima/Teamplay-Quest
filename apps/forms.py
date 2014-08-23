# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import (
    StringField,
    TextAreaField
)
from wtforms import validators
from wtforms.validators import NumberRange
from wtforms.fields.html5 import IntegerField,IntegerRangeField, DecimalField

class GroupForm(Form):
    name = StringField(
        u'그룹 이름',
        [validators.data_required(u'그룹 이름을 입력해주세요.')],
        description={'placeholder': u'그룹 이름을 입력해주세요.'}
    )

class QuestForm(Form):
    title = StringField(
        u'퀘스트 이름',
        [validators.data_required(u'퀘스트 이름을 입력해주세요.')],
        description={'placeholder': u'퀘스트 이름을 입력해주세요.'}
    )

    category = StringField(
        u'카테고리',
        [validators.data_required(u'카테고리를 입력하주세요.')],
        description={'placeholder': u'카테고리를 입력해주세요.'}
    )

    description = TextAreaField(
        u'내용',
        [validators.data_required(u'내용을 입력해주세요.')],
        description={'placeholder': u'내용을 입력해주세요.'}
    )

    expired_date = DecimalField(
        u'기한',
        validators=[NumberRange(1, 120)],
        description={'placeholder': u'1에서 120사이의 시간를 입력해주세요.'}
    )

# class JoinForm(Form):
#     email = EmailField(
#         u'이메일',
#         [validators.data_required(u'이메일을 입력하시기 바랍니다.'),
#         validators.Email(u'이메일을 입력하시기 바랍니다.')],
#         description={'placeholder': u'이메일을 입력하세요.'}
#     )
#     password = PasswordField(
#         u'비밀번호',
#         [validators.data_required(u'비밀번호를 입력하시기 바랍니다.')],
#         description={'placeholder': u'비밀번호를 입력하세요.'}
#     )
#     confirm_password = PasswordField(
#         u'비밀번호 확인',
#         [validators.data_required(u'비밀번호를 한번 더 입력하시기 바랍니다.'),
#          validators.EqualTo('password', message=u'비밀번호가 일치하지 않습니다.')],
#         description={'placeholder': u'비밀번호를 한번 더 입력하세요.'}
#     )
#     name = StringField(
#         u'이름',
#         [validators.data_required(u'이름을 입력하시기 바랍니다.')],
#         description={'placeholder': u'이름을 입력하세요.'}
#     )

# class LoginForm(Form):
#     email = EmailField(
#         u'이메일',
#         [validators.data_required(u'이메일을 입력하시기 바랍니다.'),
#         validators.Email(u'이메일을 입력하시기 바랍니다.')],
#         description={'placeholder': u'이메일을 입력하세요.'}
#     )
#     password = PasswordField(
#         u'비밀번호',
#         [validators.data_required(u'비밀번호를 입력하시기 바랍니다.')],
#         description={'placeholder': u'비밀번호를 입력하세요.'}
#     )
#
#
# class ArticleForm(Form):
#     title = StringField(
#         u'제목',
#         [validators.data_required(u'제목을 입력하시기 바랍니다.')],
#         description={'placeholder': u'제목을 입력하세요.'}
#     )
#     content = TextAreaField(
#         u'내용',
#         [validators.data_required(u'내용을 입력하시기 바랍니다.')],
#         description={'placeholder': u'내용을 입력하세요.'}
#     )
#     # author = StringField(
#     #     u'작성자',
#     #     [validators.data_required(u'이름을 입력하시기 바랍니다.')],
#     #     description={'placeholder': u'이름을 입력하세요.'}
#     # )
#     category = StringField(
#         u'카테고리',
#         [validators.data_required(u'카테고리를 입력하시기 바랍니다.')],
#         description={'placeholder': u'카테고리를 입력하세요.'}
#     )
#
#
# class CommentForm(Form):
#     content = StringField(
#         u'내용',
#         [validators.data_required(u'내용을 입력하시기 바랍니다.')],
#         description={'placeholder': u'내용을 입력하세요.'}
#     )
#     author = StringField(
#         u'작성자',
#         [validators.data_required(u'이름을 입력하시기 바랍니다.')],
#         description={'placeholder': u'이름을 입력하세요.'}
#     )
#     password = PasswordField(
#         u'비밀번호',
#         [validators.data_required(u'비밀번호를 입력하시기 바랍니다.')],
#         description={'placeholder': u'비밀번호를 입력하세요.'}
#     )
#     email = EmailField(
#         u'이메일',
#         [validators.data_required(u'이메일을 입력하시기 바랍니다.'),
#          validators.Email(u'이메일을 입력하시기 바랍니다.')],
#         description={'placeholder': u'이메일을 입력하세요.'}
#     )