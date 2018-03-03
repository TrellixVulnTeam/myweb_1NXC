# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    category = models.CharField(max_length=20, choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')), verbose_name=u'机构类别', default='pxjg')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'logo') # %Y当前年%m当前月 创建当前年月的文件夹
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    tag = models.CharField(max_length=10, verbose_name=u'机构标签', default='应有尽有，货真价实')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 教师有个外键指向courseorg，这里可以直接调用方法访问教师，返回课程机构教师数量
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name=u'头像', max_length=100, default='')
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateTimeField(default=datetime.now)
    age = models.IntegerField(default=18, verbose_name=u'年龄')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()