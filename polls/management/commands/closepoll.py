from django.core.management.base import BaseCommand
from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes or deletes one or more polls.'

    def add_arguments(self, parser):
        # 1. Tham số vị trí (bắt buộc)
        parser.add_argument('poll_ids', nargs='+', type=int, help='A list of poll IDs.')

        # 2. Tham số tùy chọn (không bắt buộc)
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete polls instead of closing them.',
        )
        parser.add_argument(
            '--reason',
            type=str,
            help='The reason for this action.',
        )

    def handle(self, *args, **options):
        poll_ids = options['poll_ids']
        is_deleting = options['delete']
        reason = options['reason']

        for poll_id in poll_ids:
            # ... (Logic tìm và xử lý poll như các ví dụ trên) ...
            self.stdout.write(f"Processing poll {poll_id}...")

        if reason:
            self.stdout.write(self.style.WARNING(f"Action reason: {reason}"))