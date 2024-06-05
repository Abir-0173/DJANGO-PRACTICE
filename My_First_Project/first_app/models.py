from django.db import models

# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    # age = models.IntegerField(max_length=3)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    reating = (
        (1, "worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent"),
    )

    num_stars = models.IntegerField(choices=reating)

   

    def __str__(self) -> str:
        return self.name + ", rating: " + str(self.num_stars)

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# CREATE TABLE myapp_person (
#     "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

# CREATE TABLE myapp_person(
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );


# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

