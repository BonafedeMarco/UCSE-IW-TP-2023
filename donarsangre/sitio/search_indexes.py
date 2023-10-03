from haystack import indexes
from sitio.models import Post
from datetime import datetime

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Se indexan todas las publicaciones no expiradas"""
        return self.get_model().objects.filter(expiration_date__gte=datetime.now())
