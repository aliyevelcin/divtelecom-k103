from django.db import models

class Product(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    brand = models.CharField(max_length=100)
    form_factor = models.CharField(max_length=100)
    operating_system = models.CharField(blank=True, max_length=100, null=True)
    cellular_technology = models.CharField(blank=True, max_length=100, null=True)
    display_type = models.CharField(blank=True, max_length=100, null=True)
    camera = models.CharField(blank=True, max_length=100, null=True)
    cpu = models.CharField(blank=True, max_length=100, null=True)
    ram = models.CharField(blank=True, max_length=100, null=True)
    battery = models.CharField(blank=True, max_length=100, null=True)
    water_and_dust_rating = models.CharField(blank=True, max_length=100, null=True)
    guarantee = models.CharField(blank=True, max_length=100, null=True)
    storage = models.ManyToManyField("Storage", verbose_name=("Storage"), db_index=True, related_name='storage_product', null=True, blank=True)
    color = models.ManyToManyField('Color',  verbose_name=("Color"), db_index=True, related_name="color_product", null=True, blank=True)    
    category = models.ForeignKey("Category", on_delete=models.CASCADE, db_index=True, related_name='category_product', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.model
    
  
class ProductVersion(models.Model):
    product = models.ForeignKey('Product',related_name='product_versions',on_delete=models.CASCADE,db_index=True,null=True,blank=True,related_query_name='product_version') #product = models.ForeingKey(Product, on_delete = models.CASCADE,db_index = True,null=True,blank=True)
    color = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    quantity = models.IntegerField('Quantity',blank=True,null=False)
    class Meta:
        verbose_name = 'Product Version'
        verbose_name_plural = 'Product Versions'

    def __str__(self):
        return self.color
    
    def get_finaly_price(self):
        quantity = int(self.quantity)
        price = int(self.product.price)
        return quantity * price
    
class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Storage(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'
    def __str__(self):
        return self.title
    
class Color(models.Model):
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return f"{self.color}" 

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'  

    def __str__(self):
        return f"{self.image}"
class ColorImage(models.Model):
    image = models.ImageField(upload_to='images')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, db_index=True, related_name='color_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Color Image'
        verbose_name_plural = 'Color Images'  

    def __str__(self):
        return f"{self.image}"
    
class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question