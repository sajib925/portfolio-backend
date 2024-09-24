from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .models import Contact
from .serializers import ContactSerializer
from django.conf import settings

class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Send confirmation email to the user
            user_subject = "Thank you for contacting us!"
            user_message = f"Dear {contact.first_name} {contact.last_name},\n\nThank you for reaching out to us. We have received your message and will respond shortly.\n\nMessage:\n{contact.message}\n\nBest regards,\nYour Team"
            user_recipient = contact.email

            send_mail(
                user_subject,
                user_message,
                settings.DEFAULT_FROM_EMAIL,  # From email
                [user_recipient],
                fail_silently=False,
            )

            # Render the HTML email template for the admin
            admin_message_html = render_to_string('contact_email.html', {
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'email': contact.email,
                'subject': contact.subject,
                'message': contact.message,
            })

            # Send the user's message to the admin
            admin_subject = f"New Contact Form Submission from {contact.first_name} {contact.last_name}"
            email = EmailMessage(
                admin_subject,
                admin_message_html,
                settings.DEFAULT_FROM_EMAIL,  # From email
                [settings.ADMIN_EMAIL],  # Admin email
            )
            email.content_subtype = "html"  # Main content is now text/html

            email.send(fail_silently=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
