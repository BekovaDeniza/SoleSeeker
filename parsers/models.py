from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class ParserConfig(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='site')
    file_path = models.FilePathField(path='sources/', match='*.py')
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"Config for {self.name}"

    def run_catalog_parser(self):
        # Реализовать код для запуска парсинга каталога сайта
        pass

    def run_product_parser(self, product_url):
        # Реализовать код для запуска парсинга отдельного товара по его URL
        pass
