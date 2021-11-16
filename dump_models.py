# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Audiences(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    student_id = models.IntegerField(blank=True, null=True)
    class_field = models.ForeignKey('Classes', models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.
    is_vnuis_student = models.IntegerField(blank=True, null=True)
    total_events_registered = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audiences'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classes(models.Model):
    class_code = models.CharField(primary_key=True, max_length=12)
    class_major = models.ForeignKey('Majors', models.DO_NOTHING, db_column='class_major')
    total_students = models.IntegerField(blank=True, null=True)
    graduated_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'classes'


class Departments(models.Model):
    id = models.IntegerField()
    department_code = models.CharField(primary_key=True, max_length=5)
    department_name = models.CharField(max_length=255)
    lead = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EventCoordinators(models.Model):
    event = models.ForeignKey('Events', models.DO_NOTHING)
    member_account = models.ForeignKey('Members', models.DO_NOTHING, db_column='member_account')
    role = models.TextField(blank=True, null=True)
    is_organizer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_coordinators'


class EventRegistrationList(models.Model):
    audience = models.ForeignKey(Audiences, models.DO_NOTHING, blank=True, null=True)
    registered_at = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey('Events', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_registration_list'


class Events(models.Model):
    event_name = models.CharField(max_length=500, blank=True, null=True)
    event_pic = models.CharField(max_length=64, blank=True, null=True)
    event_target_audience = models.CharField(max_length=255, blank=True, null=True)
    event_coordinators = models.IntegerField(blank=True, null=True)
    date_hosted = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    event_registration_list = models.IntegerField(blank=True, null=True)
    event_assets = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_survey_report = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Leaders(models.Model):
    lead_account = models.ForeignKey('Members', models.DO_NOTHING, db_column='lead_account', blank=True, null=True)
    lead_department = models.ForeignKey(Departments, models.DO_NOTHING, db_column='lead_department')

    class Meta:
        managed = False
        db_table = 'leaders'


class Majors(models.Model):
    major_code = models.CharField(primary_key=True, max_length=64)
    major_group = models.CharField(max_length=64)
    major_name_en = models.CharField(max_length=255)
    major_name_vi = models.CharField(max_length=255)
    desc_en = models.TextField(blank=True, null=True)
    desc_vi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'majors'


class Members(models.Model):
    account = models.CharField(unique=True, max_length=64, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    student_id = models.IntegerField(unique=True)
    ms_teams_email = models.CharField(max_length=64, blank=True, null=True)
    facebook_account = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=255)
    trello_account = models.CharField(max_length=64, blank=True, null=True)
    city_code = models.CharField(max_length=64, blank=True, null=True)
    department_code = models.ForeignKey(Departments, models.DO_NOTHING, db_column='department_code')
    generation = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    joined_since = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'


class Skills(models.Model):
    skill_name = models.CharField(max_length=255, blank=True, null=True)
    skill_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Skillset(models.Model):
    account = models.ForeignKey(Members, models.DO_NOTHING, db_column='account')
    skill = models.ForeignKey(Skills, models.DO_NOTHING, db_column='skill')
    is_primary_skill = models.IntegerField(blank=True, null=True)
    is_secondary_skill = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skillset'
