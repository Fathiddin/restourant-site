from django.db import models

# Create your models here.

# Taomlar kategiryasi
class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Kategoriya nomi')
    slug = models.SlugField(unique=True, verbose_name='Kategoriya slugi')
    
    def __str__(self):
        return str(self.title)
    

# taomlar
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Taom nomi')
    image = models.ImageField(upload_to='foods-images/')
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='products')    
    price = models.PositiveIntegerField(default=0, verbose_name='narxi')
    discount = models.PositiveIntegerField("Necha foiz chegirma ?",default=0)
    description = models.TextField()
    
    def get_discount_price(self):
        price = self.price
        if self.discount:            
            p = self.discount * self.price // 100
            price = price - p
            return price
        else:
            return 0
    
    def __str__(self):
        return str(self.name)


# savatchagi mahsulotlar
class CardProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_products'
    )
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.product.name)


# savatcha
class Cart(models.Model):
    products = models.ManyToManyField(CardProduct, related_name='products')
    total_quantity = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    # savatchaga qo'shish
    def add(self,product_id,qty):
        status = {}
        
        product = Product.objects.get(id=product_id)
        
        for item in self.products.all():
            print(item.product.id, "---", product.id)
           
            if item.product.id == product.id:
                status["found"] = True
            else:
                status["found"] = False
        
        if status.get("found"):
            status["done"] = False
        else:        
            price = 0
            if product.discount:            
                price = product.get_discount_price() * qty
            else:
                price = product.price * qty
            self.products.create(
                product=product,
                quantity=qty,
                price=price
            )
            
            self.total_quantity += qty
            self.total_price += price
            self.save()
            status["done"] = True
        return status
    # savatchadan o'chirish
    def deleteItem(self, product_id,qty):
        product = Product.objects.get(id=product_id)
        for item in self.products.all():
            if item.product.id == product.id:
                item.delete()
        price = product.price * qty
        # self.products.remove(product)
        self.total_quantity -= qty
        self.total_price -= price
        self.save()
        return True
    
    def __str__(self):
        return f"Cart = {self.id}"
    

# harid qilish
class Order(models.Model):
    STATUS = (
        ('Yetkazib berildi', 'Yetkazib berildi'),
        ('Korib chiqilyapti', 'Korib chiqilyapti'),
        ('Korilmadi', 'Korilmadi'),
    )
    cart = models.ForeignKey(Cart, verbose_name='Savatcha', on_delete=models.PROTECT)
    full_name = models.CharField(verbose_name='Toliq ism', max_length=255)
    city = models.CharField(verbose_name='Shahar', max_length=255)
    address = models.CharField(verbose_name='Manzil', max_length=255)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name='Holat', max_length=255, choices=STATUS, default='Korilmadi')

    def __str__(self):
        return f"{self.full_name}"


class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return str(self.name)
    
    
class Album(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='album')
    
    def __str__(self):
        return str(self.name)
    