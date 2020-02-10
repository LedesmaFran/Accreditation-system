from django.db import models

# Create your models here.

import datetime
from django.utils import timezone


class Event(models.Model):
    class PossiblePlaces(models.TextChoices):
        AULA012 = '012', 'Main Building. First Floor: Classroom 12'
        AULA013 = '013', 'Main Building. First Floor: Classroom 13'
        AULAMAG = 'Mag', 'Main Building. Second Floor: Classroom '
        AULA022 = '022', 'Main Building. Second Floor: Classroom 22'
        AULA023 = '023', 'Main Building. Second Floor: Classroom 23'
        AULA024 = '024', 'Main Building. Second Floor: Classroom 24'
        AULA025 = '025', 'Main Building. Second Floor: Classroom 25'
        AULA026 = '026', 'Main Building. Second Floor: Classroom 26'
        AULA029 = '029', 'Main Building. Second Floor: Classroom 29'
        AULA030 = '030', 'Main Building. Third Floor: Classroom 30'
        AULA031 = '031', 'Main Building. Third Floor: Classroom 31'
        AULA032 = '032', 'Main Building. Third Floor: Classroom 32'
        AULA033 = '033', 'Main Building. Third Floor: Classroom 33'
        AULA104 = '104', 'Annex Building. Ground Floor: Classroom 104'
        AULA105 = '105', 'Annex Building. Ground Floor: Classroom 105'
        AULA110 = '110', 'Annex Building. First Floor: Classroom 110'
        AULA111 = '111', 'Annex Building. First Floor: Classroom 111'
        AULA117 = '117', 'Annex Building. First Floor: Classroom 117'
        AULA120 = '120', 'Annex Building. Second Floor: Classroom 120'
        AULA121 = '121', 'Annex Building. Second Floor: Classroom 121'
        AULA133 = '133', 'Annex Building. Third Floor: Classroom 133'
        AULA140 = '140', 'Annex Building. Forth Floor: Classroom 140'
        AULA152 = '152', 'Annex Building. Fifth Floor: Classroom 152'

    name = models.CharField(max_length=200, default='')
    description = models.TextField(max_length=1000, default='')
    speaker = models.CharField(max_length=200, default='')
    place = models.CharField(max_length=100,
                             choices=PossiblePlaces.choices,
                             default=PossiblePlaces.AULA012)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    registered = models.ManyToManyField('participant')
    accredit = models.ManyToManyField('participant', related_name='accredited', blank=True)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.name


class participant(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=200, default='', blank=True)
    title = models.CharField(max_length=200, default='', blank=True)
    speaker = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
