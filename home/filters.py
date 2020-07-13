import django_filters
from jobs.models import job


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = ['title', 'city', 'job_type']