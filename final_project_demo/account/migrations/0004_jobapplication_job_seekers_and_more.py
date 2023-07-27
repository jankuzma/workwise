# Generated by Django 4.2.2 on 2023-07-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_jobseekerjoblisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job_seekers',
            field=models.ManyToManyField(related_name='job_applications', to='account.jobseekeruser'),
        ),
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together={('job_listing', 'application_date')},
        ),
        migrations.DeleteModel(
            name='JobSeekerJobListing',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_seeker',
        ),
    ]
