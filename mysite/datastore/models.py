from django.db import models
#from jsonfield import JSONField
from picklefield.fields import PickledObjectField

class acquisition(models.Model):
    #acq_id = models.CharField(max_length=6)
    acqdatetime = models.DateTimeField('date and time acquired')

    def __unicode__(self):
        return str(self.acqdatetime)

class coordinate(models.Model):
    coordinate_label = models.CharField(max_length=20)
    coordinate_unit = models.CharField(max_length=20)
    #coordinate = JSONField()
    coordinate_val = PickledObjectField()
    aquisition = models.ForeignKey(acquisition, related_name='coordinates')
    def __unicode__(self):
        return self.coordinate_label

class value(models.Model):
    value_label = models.CharField(max_length=20)
    value_unit = models.CharField(max_length=20)
    #value = JSONField()
    value = PickledObjectField()
    aquisition = models.ForeignKey(acquisition, related_name='values')
    def __unicode__(self):
        return self.value_label

# class meta(models.Model):
#     meta_label = models.CharField(max_length=20)
#     meta_unit = models.CharField(max_length=20)
#     meta = models.FloatField()
#     aquisition = models.ForeignKey(acquisition, related_name='metadata')
#     def __unicode__(self):
#         return self.meta_label

# References
# http://mitchfournier.com/2011/10/11/how-to-import-a-csv-or-tsv-file-into-a-django-model/
# https://github.com/bradjasper/django-jsonfield
