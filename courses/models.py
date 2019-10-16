from django.db import models

# Create your models here.

class Course(models.Model):  
  name = models.CharField(max_length=50)
  created_on = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)

class Hole(models.Model):
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  ELEVEN = 11
  TWELVE = 12
  THIRTEEN = 13
  FOURTEEN = 14
  FIFTEEN = 15
  SIXTEEN = 16
  SEVENTEEN = 17
  EIGHTEEN = 18
  FRONT = 1
  BACK = 2
  HOLES = (
    (ONE, 'Hole 1'),
    (TWO, 'Hole 2'),
    (THREE, 'Hole 3'),
    (FOUR, 'Hole 4'),
    (FIVE, 'Hole 5'),
    (SIX, 'Hole 6'),
    (SEVEN, 'Hole 7'),
    (EIGHT, 'Hole 8'),
    (NINE, 'Hole 9'),
    (TEN, 'Hole 10'),
    (ELEVEN, 'Hole 11'),
    (TWELVE, 'Hole 12'),
    (THIRTEEN, 'Hole 13'),
    (FOURTEEN, 'Hole 14'),
    (FIFTEEN, 'Hole 15'),
    (SIXTEEN, 'Hole 16'),
    (SEVENTEEN, 'Hole 17'),
    (EIGHTEEN, 'Hole 18'),
  )
  HANDICAPS = (
    (ONE, '1'),
    (TWO, '2'),
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5'),
    (SIX, '6'),
    (SEVEN, '7'),
    (EIGHT, '8'),
    (NINE, '9'),
    (TEN, '10'),
    (ELEVEN, '11'),
    (TWELVE, '12'),
    (THIRTEEN, '13'),
    (FOURTEEN, '14'),
    (FIFTEEN, '15'),
    (SIXTEEN, '16'),
    (SEVENTEEN, '17'),
    (EIGHTEEN, '18'),
  )
  PARS = (
    (THREE, '3'),
    (FOUR, '4'),
    (FIVE, '5'),
  )
  SIDES = (
    (FRONT, 'Front'),
    (BACK, 'Back'),
  )
  side = models.PositiveSmallIntegerField(
    choices=SIDES,
    default=FRONT
  )
  hole_number = models.PositiveSmallIntegerField(
    choices=HOLES,
    default=ONE
  )
  handicap = models.PositiveSmallIntegerField(
    choices=HANDICAPS,
    default=ONE
  )  
  par = models.PositiveSmallIntegerField(
    choices=PARS,
    default=FOUR
  )  
  
class CourseTee(models.Model):
  MALE = 'M'
  FEMALE = 'F'
  NINE = 9
  EIGHTEEN = 18
  GENDERS = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
  )
  NUM_OF_HOLES = (
    (NINE, 'Nine Holes'),
    (EIGHTEEN, 'Eighteen Holes')
  )  
  tee_name = models.CharField(max_length=50)
  gender = models.CharField(
    max_length=1,
    choices=GENDERS,
    default=MALE
  )
  rating = models.DecimalField(max_digits=4, decimal_places=1)
  slope = models.PositiveSmallIntegerField()
  holecount = models.PositiveSmallIntegerField(
    choices=NUM_OF_HOLES,
    default=EIGHTEEN
  )
  holes = models.ForeignKey('Hole', on_delete=models.CASCADE)
  couse = models.ForeignKey('Course', on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)  
  

  
  
  
  
