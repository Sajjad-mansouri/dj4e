import csv
from cats.models import Cat,Breed


def run():
	file=open('scripts/meow.csv','r') 
	csv_reader=csv.reader(file)
	next(csv_reader)
	Cat.objects.all().delete()
	Breed.objects.all().delete()
	for row in csv_reader:
		b,created=Breed.objects.get_or_create(name=row[1])
		c = Cat(nickname=row[0], breed=b, weight=int(float(row[2])))
		c.save()

