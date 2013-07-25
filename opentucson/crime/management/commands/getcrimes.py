import zipfile
import csv
import datetime

from django.core.management import BaseCommand, CommandError
from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.geos import error

from crime.models import Crime, Neighborhood

import requests


class crime_csv(csv.excel):
    delimiter = ';'
    doublequote = False
    skipinitialspace = True
    lineterminator = '\r\n'
    quoting = csv.QUOTE_NONE


csv.register_dialect('crime_csv', crime_csv)


class Command(BaseCommand):
    help = "Load in most recent crime data from Tucsons website"

    def handle(self, *args, **options):
        url = 'http://cms3.tucsonaz.gov/files/transportation/files/TPD_Incidents_45Day.zip'
        zipname = "data.zip"
        filename = 'tpd_100blk_incid.txt'
        r = requests.get(url, stream=True)

        with open(zipname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

        zf = zipfile.ZipFile(zipname)
        data = zf.open(filename, 'rU')

        for csv_row in csv.DictReader(data, dialect=crime_csv):
            row = dict((k.lower(), v) for k, v in csv_row.iteritems())

            for k, v in row.iteritems():
                if v == 'NULL':
                    row[k] = None
                else:
                    row[k] = v

            if row['date_rept']:
                report_date = row['date_rept'].split(' ')[0]

                if not row['hour_rept']:
                    row['hour_rept'] = '0000'

                if row['hour_rept'][0:2] == '24':
                    row['hour_rept'] = '2359'

                report_datetime = datetime.datetime.strptime("{0} {1}:{2}".format(report_date,
                                                                            row['hour_rept'][0:2],
                                                                            row['hour_rept'][2:4]),
                                                                            '%Y-%m-%d %H:%M')
                row['report_date'] = report_datetime

            else:
                row['report_date'] = None

            if row['date_occu']:
                occur_date = row['date_occu'].split(' ')[0]

                if not row['hour_occu']:
                    row['hour_occu'] = row['hour_rept']

                if row['hour_occu'][0:2] == '24':
                    row['hour_occu'] = '2359'

                occur_datetime = datetime.datetime.strptime("{0} {1}:{2}".format(occur_date,
                                                                           row['hour_occu'][0:2],
                                                                           row['hour_occu'][2:4]),
                                                                           '%Y-%m-%d %H:%M')
                row['start_date'] = occur_datetime

            else:
                row['start_date'] = None

            if row['date_fnd']:
                end_date = row['date_fnd'].split(' ')[0]

                if not row['hour_fnd']:
                    row['hour_fnd'] = row['hour_rept']

                if row['hour_fnd'][0:2] == '24':
                    row['hour_fnd'] = '2359'

                end_datetime = datetime.datetime.strptime("{0} {1}:{2}".format(end_date,
                                                                         row['hour_fnd'][0:2],
                                                                         row['hour_fnd'][2:4]),
                                                                         '%Y-%m-%d %H:%M')
                row['end_date'] = end_datetime

            else:
                row['end_date'] = None

            try:
                row['location'] = fromstr('POINT({0} {1})'.format(row['xcoord'], row['ycoord']), srid=102649)
            except error.GEOSException:
                pass

            crime, created = Crime.objects.get_or_create(**row)

            if created:
                print 'CREATED {0}'.format(row['inci_id'])
                return
                try:
                    crime.neighborhood = Neighborhood.objects.get(geom__contains='POINT({0} {1})'.format(
                                                                                row['xcoord'], row['ycoord'])
                    )
                    crime.save()
                except:
                    print 'UNABLE TO ADD NEIGHBORHOOD'
                    pass

            else:
                print '{0} ALREADY EXISTS, SKIPPING'.format(row['inci_id'])

