# bookstore/models.py

from django.db import models
import datetime

# Model này lưu thông tin về tác giả.
# Mỗi tác giả có thể viết nhiều cuốn sách.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)

    # Phương thức __str__ giúp hiển thị tên đối tượng một cách thân thiện
    # trong trang admin hoặc khi bạn print() nó ra.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        # Sắp xếp các tác giả theo họ, sau đó đến tên
        ordering = ["last_name", "first_name"]

# Model này lưu thông tin về một cuốn sách.
# Mỗi cuốn sách chỉ có một tác giả (mối quan hệ nhiều-một).
class Book(models.Model):
    title = models.CharField(max_length=200)
    
    # Đây là mối quan hệ nhiều-một (Many-to-one).
    # Một cuốn sách có một tác giả, nhưng một tác giả có thể có nhiều sách.
    # on_delete=models.CASCADE nghĩa là khi một tác giả bị xóa,
    # tất cả sách của tác giả đó cũng sẽ bị xóa.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    publication_date = models.DateField()
    
    # IntegerField để lưu số trang.
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        # Sắp xếp các cuốn sách theo ngày xuất bản, cuốn mới nhất lên đầu
        ordering = ["-publication_date"]