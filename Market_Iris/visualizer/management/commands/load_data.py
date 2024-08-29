import csv
from django.core.management.base import BaseCommand
from visualizer.models import BankRecord

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = 'C:/Users/shadr/Market_Iris/data/bank.csv'
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                BankRecord.objects.create(
                    age=row['age'],
                    job=row['job'],
                    marital=row['marital'],
                    education=row['education'],
                    default=row['default'],
                    balance=row['balance'],
                    housing=row['housing'],
                    loan=row['loan'],
                    contact=row['contact'],
                    day=row['day'],
                    month=row['month'],
                    duration=row['duration'],
                    campaign=row['campaign'],
                    pdays=row['pdays'],
                    previous=row['previous'],
                    poutcome=row['poutcome'],
                    deposit=row['deposit']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))