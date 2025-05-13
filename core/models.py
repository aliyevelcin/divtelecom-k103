from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField('Description')
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100, null=True, blank=True)
    cellular_technology = models.CharField(max_length=100, null=True, blank=True)
    display_type = models.CharField(max_length=100, null=True, blank=True)
    camera = models.CharField(max_length=100, null=True, blank=True)
    cpu = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    battery = models.CharField(max_length=100, null=True, blank=True)
    water_and_dust_rating = models.CharField(max_length=100, null=True, blank=True)
    guarantee = models.CharField(max_length=100, null=True, blank=True)
    storage = models.ManyToManyField("Storage", verbose_name=("Storage"), db_index=True, related_name='storage_product', null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, db_index=True, related_name='category_product', null=True, blank=True)
    color = models.ManyToManyField('Color',  verbose_name=("Color"), db_index=True, related_name="color_product", null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    rating = models.IntegerField('Rating',blank=True,null=False)
    # wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, db_index=True, related_name='wishlist_products', null=True, blank=True)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, db_index=True, related_name='cart_products', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.title)}-{self.id}'
        super(Product, self).save(*args, **kwargs)