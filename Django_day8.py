# Demonstrating Lazy QuerySet construction
from myapp.models import Article

# No SQL query executed yet!
articles = Article.objects.filter(is_published=True).select_related('author')

# Chaining operations builds the internal SQL representation lazily
title_list = articles.filter(views__gt=1000).values_list('title', flat=True)

# SQL database query is executed ONLY upon iteration
for title in title_list:
    print(title)