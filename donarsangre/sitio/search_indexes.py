from haystack import indexes
from sitio.models import Post
from datetime import datetime

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    blood_type = indexes.CharField(model_attr='blood_type')
    liters_required = indexes.FloatField(model_attr='liters_required')
    location = indexes.CharField(model_attr='location')
    body = indexes.CharField(model_attr='body')
    pk = indexes.IntegerField(model_attr='pk')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Se indexan todas las publicaciones no expiradas"""
        return self.get_model().objects.filter(expiration_date__gte=datetime.now())
