from .models import Operation
import csv
from datetime import datetime

def import_data():
    filename ='media/data.csv'
    with open(filename, newline='') as f:
        reader = csv.reader(f,delimiter = ',')
        try:
            for row in reader:
                _, created = Operation.objects.get_or_create(
                OptProductCode=row[0],
                OptConsum=row[3],
                OptGood=row[4],
                OptScraps=row[5],
                OptDownTime=row[6],
                OptDuration=row[7]
                )
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
