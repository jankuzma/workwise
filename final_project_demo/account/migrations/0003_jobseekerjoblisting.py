# Generated by Django 4.2.2 on 2023-07-27 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_jobseekeruser_tech_stack_delete_techstack'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeekerJobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='account.joblisting')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_listings_applied', to='account.jobseekeruser')),
            ],
            options={
                'unique_together': {('job_seeker', 'job_listing')},
            },
        ),
    ]
