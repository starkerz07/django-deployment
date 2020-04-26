# Generated by Django 3.0.4 on 2020-04-25 16:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DomesticComplaint',
            fields=[
                ('doc_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('o_name', models.CharField(max_length=128, verbose_name='Complainant Name')),
                ('o_email', models.EmailField(max_length=64, verbose_name='Complainant Email')),
                ('o_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Complainant No')),
                ('o_state', models.CharField(max_length=32, verbose_name='Complainant Name')),
                ('o_city', models.CharField(max_length=32, verbose_name='Complainant City')),
                ('o_adds', models.TextField(max_length=256, verbose_name='Complainant Address')),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='MALE', max_length=8, verbose_name='Gender')),
                ('acc_name', models.CharField(max_length=128, verbose_name='Accused Name')),
                ('acc_adds', models.TextField(blank=True, max_length=256, null=True, verbose_name='Accused address')),
                ('acc_state', models.CharField(max_length=32, verbose_name='Accused state')),
                ('acc_city', models.CharField(max_length=32, verbose_name='Accused city')),
                ('acc_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Accused Email')),
                ('acc_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Accused contact No')),
                ('acc_gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='MALE', max_length=8, verbose_name='Accused gender')),
                ('case_pending_a', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=4, verbose_name='case pending at any other court')),
                ('case_pending_w', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=4, verbose_name='case pending at any women association court')),
                ('c_description', models.TextField(max_length=4056, validators=[django.core.validators.MinLengthValidator(30)], verbose_name='Complainant Description')),
                ('c_document', models.FileField(blank=True, null=True, upload_to='domestic/', verbose_name='Complaint related documents')),
                ('c_filed', models.DateField(auto_now_add=True, verbose_name='Complaint filed date')),
                ('c_amt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Complaint Amount')),
                ('p_date', models.DateTimeField(blank=True, null=True, verbose_name='Payment Date')),
                ('p_status', models.BooleanField(default=0, verbose_name='Payment Status')),
                ('new_cid', models.CharField(blank=True, max_length=128, null=True, verbose_name='Order ID')),
                ('txn_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Transaction ID')),
                ('update_flag', models.BooleanField(default=0, verbose_name='Information Updated')),
                ('admin_reply', models.TextField(blank=True, max_length=4056, null=True, validators=[django.core.validators.MinLengthValidator(30)], verbose_name='Update Complaint Status')),
                ('admin_document', models.FileField(blank=True, null=True, upload_to='admin/domestic/', verbose_name='Attach documents')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]