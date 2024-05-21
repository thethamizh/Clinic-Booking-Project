from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'thamizhdasane@gmail.com',
    ['thamizhdasane@gmail.com'],
    fail_silently=False,
)
