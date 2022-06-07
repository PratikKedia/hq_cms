from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    # details of the question
    cwf = models.ManyToManyField("Cwf") # for ManyToManyField Django will automatically create a table to manage to manage many-to-many relationships
    kt = models.ManyToManyField("Kt")
    role = models.ManyToManyField("Role")
    stage = models.ForeignKey("Stage", on_delete = models.SET_NULL, null=True) # if the stage id is delelted it will set this field to NULL
    # assests for the question
    exhibits = models.ManyToManyField("Exhibit")
    excels = models.ManyToManyField("Excel")
    context = models.JSONField()
    # content of the question
    text = models.CharField(max_length = 100, blank = False, null = False)
    qtype = models.ForeignKey("Qtype", on_delete = models.SET_NULL, null=True)
    options = models.JSONField()
    score_type = models.CharField(max_length = 10, blank = False, null = False)
    score_weight = models.FloatField(validators = [MinValueValidator(0)])
    # extras
    resources = models.JSONField()
    # timestamp and tracking
    creator = models.ForeignKey("User", on_delete = models.SET_NULL, null=True, related_name='question_creator') # if the creator user is deleted it will set this field to NULL
    approved_by = models.ForeignKey("User", on_delete = models.SET_NULL, null=True, related_name='question_approver') # if the user is deleted it will set this field to NULL
    last_edited_by = models.ForeignKey("User", on_delete = models.SET_NULL, null=True, related_name='question_editor') # if the user is deleted it will set this field to NULL
    last_edited = models.DateTimeField(default=datetime.now, blank = False)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    aid = models.AutoField(primary_key=True)
    problem_statement = models.CharField(max_length=1000, blank = True)
    questions = models.ManyToManyField("Question")
    role = models.ManyToManyField("Role")
    remarks = models.CharField(max_length=1000, blank = True)
    # timestamp and tracking
    creator = models.ForeignKey("User", on_delete = models.SET_NULL, null=True, related_name='assessment_creator') # if the creator user is deleted it will set this field to NULL
    approved_by = models.ForeignKey("User", on_delete = models.SET_NULL, null=True, related_name='assessment_approver') # if the user is deleted it will set this field to NULL
    last_updated = models.DateTimeField(default=datetime.now, blank = False)

    def __str__(self):
        return self.name

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_code = models.CharField(max_length = 20, blank = False, null = False, unique=True)
    role_name = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.name

class Exhibit(models.Model):
    exhibit_id = models.AutoField(primary_key=True)
    # we have 2 choices here, if we want to store the assests externally on the cloud we need to have a URL field, otherwise we can also use Django media manager with imagefield
    url = models.URLField(max_length = 250)
    #file = models.FileField(upload_to = 'exhibits/')
    #image = models.ImageField(upload_to = 'exhibits/')
    alt_text = models.CharField(max_length = 100, blank = True)
    type = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.name

class Excel(models.Model):
    excel_id = models.AutoField(primary_key=True)
    url = models.URLField(max_length = 250)
    alt_text = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.name

# for the users we can also use the Django's inbuilt user management system
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, blank = False)
    email = models.EmailField(max_length = 200)
    access_role = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# class QuesToRole(models.Model): not required

class Cwf(models.Model):
    cwf_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length = 100, unique=True, blank = False, null = False)
    name = models.CharField(max_length = 255, blank = False, null = False)
    role = models.ManyToManyField("Role")

    def __str__(self):
        return self.name


class Kt(models.Model):
    kt_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length = 100, unique=True, blank = False, null = False)
    name = models.CharField(max_length = 255, blank = False, null = False)
    role = models.ManyToManyField("Role")
    cwf = models.ManyToManyField("Cwf")

    def __str__(self):
        return self.name

class Stage(models.Model):
    stage_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length = 100, unique=True, blank = False, null = False)
    name = models.CharField(max_length = 255, blank = False, null = False)
    role = models.ManyToManyField("Role")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Qtype(models.Model):
    qtype_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length = 100, unique=True, blank = False, null = False)
    name = models.CharField(max_length = 255, blank = False, null = False)

    def __str__(self):
        return self.name
