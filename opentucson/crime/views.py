from dateutil import parser

from crime.serializers import CrimeSerializer
from crime.models import Crime

from rest_framework import generics
import django_filters



class CrimeList(generics.ListAPIView):
    serializer_class = CrimeSerializer
    paginate_by = 100
    paginate_by_param = 'page_size'

    def get_queryset(self):
        queryset = Crime.objects.all()

        date_start = self.request.QUERY_PARAMS.get('start_date', None)
        date_end = self.request.QUERY_PARAMS.get('end_date', None)

        if date_start:
            queryset = queryset.filter(start_date__gt=parser.parse(date_start))
        if date_end:
            queryset = queryset.filter(start_date__lt=parser.parse(date_end))

        return queryset


class CrimeDetail(generics.RetrieveAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer
