from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Tag(models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length= 255)
    slug = models.CharField(max_length= 255, unique= True, blank= True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
            
    
class Category(models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length= 255)
    slug = models.CharField(max_length= 255, unique= True, blank= True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICE =[
        ('draft','Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]
    
    id = models.BigAutoField(primary_key= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, blank= True)
    title = models.CharField(max_length= 255, blank= True)
    slug = models.CharField(max_length= 255, unique= True, blank= True)
    content = models.TextField()
    image = models.ImageField(upload_to= "Post_Images/", blank= True, null= True)
    status = models.CharField(max_length=15, choices= STATUS_CHOICE, default= 'draft')
    category = models.OneToOneField(Category, on_delete= models.SET_NULL, blank= True, null= True, related_name= 'categories')
    tag = models.ForeignKey(Tag, on_delete= models.SET_NULL, null= True, blank= True, related_name= 'tags')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
    
    
class Comment(models.Model):
    id = models.BigAutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'comments')
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'comments')
    content = models.TextField(max_length= 500)
    created_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Commented by {self.user} on {self.post}'
    
class Like(models.Model):
    id = models.BigAutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'likes')
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= 'likes')
    created_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        unique_together = ('post', 'user')
        
    def __str__(self):
        return f'{self.user} liked {self.post}'
    