import django_filters
from owner.models import Mobile

class MobileFilter(django_filters.FilterSet):
    company=django_filters.CharFilter(lookup_expr='icontains')
    model_name=django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Mobile
        fields=['price']