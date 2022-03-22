from django.db import models


class JobAds(models.Model):
    job_title = models.CharField(max_length=500)
    employer = models.CharField(max_length=500)
    job_address = models.CharField(max_length=500)
    job_details = models.CharField(max_length=500)
    end_date = models.DateField()

    class Meta:
        db_table='ads_tb'