from .models import *
import csv
import datetime

def import_data(filename):
    filename =filename
    with open(filename, newline='') as f:
        reader = csv.reader(f,delimiter = ',')
        try:
            for row in reader:
                Operation.objects.get_or_create(
                LineCode=Line.objects.get_or_create(LineCode=row[0])[0],
                MachineCode=Machine.objects.get_or_create(MachineCode=row[1])[0],
                ProductCode=Product.objects.get_or_create(ProductCode=row[2])[0],
                DateTime=datetime.datetime.strptime(row[3], "%d/%m/%Y").strftime("%Y-%m-%d"),
                Consum=row[4],
                Good=row[5],
                Scraps=row[6],
                Duration=row[8],
                DownTime=row[7],
                )
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
