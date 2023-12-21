# import_marriage_survey.py
import csv
from django.core.management.base import BaseCommand
from home.models import MarriageSurvey

class Command(BaseCommand):
    help = 'Import marriage survey data from CSV file'

    def handle(self, *args, **options):
        csv_file_path = r'C:\Users\DAIYUNWU\Desktop\Python-data-analysis\房價與結婚意願之相關分析_1214修改版 的副本 (回覆) - 表單回應 1.csv'  # Replace with the actual path to your CSV file

        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            next(reader)
            for row in reader:
                # Create a new MarriageSurvey instance for each row in the CSV
                MarriageSurvey.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV file'))
