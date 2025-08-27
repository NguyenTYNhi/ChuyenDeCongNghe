# polls/management/commands/book_report.py

from django.core.management.base import BaseCommand
from polls.models import Author, Book
from django.db.models import Count, Value
from django.db.models.functions import Concat

class Command(BaseCommand):
    help = 'Prints a report of authors and their book counts.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--order-by',
            default='last_name',
            help='Specify the field to order authors by (e.g., last_name, num_books, full_name).',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--- Author & Book Report ---'))

        order_field = options['order_by']
        
        # === PHIÊN BẢN SỬA LỖI MỚI ===
        # Bước 1: Luôn luôn annotate để tạo ra các trường tính toán mà chúng ta có thể cần.
        # Bằng cách này, queryset sẽ luôn có sẵn các trường 'num_books' và 'full_name'.
        authors_qs = Author.objects.annotate(
            num_books=Count('book'),
            full_name=Concat('first_name', Value(' '), 'last_name')
        )

        # Bước 2: Kiểm tra xem trường sắp xếp người dùng yêu cầu có hợp lệ không.
        # Đây là một bước phòng thủ tốt để tránh lỗi.
        valid_order_fields = ['first_name', 'last_name', 'email', 'birth_date', 'num_books', 'full_name']
        if order_field not in valid_order_fields:
            self.stderr.write(self.style.ERROR(
                f"Invalid order field '{order_field}'. "
                f"Please use one of: {', '.join(valid_order_fields)}"
            ))
            return # Dừng lệnh nếu tham số không hợp lệ

        # Bước 3: Áp dụng sắp xếp
        authors = authors_qs.order_by(order_field)
        
        # Đoạn code từ đây trở xuống không có gì thay đổi
        if not authors:
            self.stdout.write(self.style.WARNING('No authors found in the database.'))
            return

        self.stdout.write(f'Found {authors.count()} authors. Ordered by: {order_field}')
        self.stdout.write('---------------------------------')

        for author in authors:
            # Lưu ý: author.full_name bây giờ là một thuộc tính từ annotate,
            # nhưng chúng ta vẫn có thể dùng author.get_full_name() như bình thường.
            # Để nhất quán, ta vẫn dùng get_full_name().
            self.stdout.write(self.style.SUCCESS(f'Author: {author.get_full_name()} (Email: {author.email})'))
            self.stdout.write(f'  - Total books: {author.num_books}')
            
            books = Book.objects.filter(author=author)
            if books:
                for book in books:
                    self.stdout.write(f'    + {book.title} ({book.publication_date.year})')
            else:
                self.stdout.write(self.style.NOTICE('    No books found for this author.'))
            
            self.stdout.write('')

        self.stdout.write(self.style.SUCCESS('--- End of Report ---'))