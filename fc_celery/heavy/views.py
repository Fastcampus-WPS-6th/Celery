from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class EmailView(APIView):
    def post(self, request):
        email_list = request.data.getlist('email')
        subject = request.data['subject']
        message = request.data['message']

        send_mail(
            subject=subject,
            message=message,
            from_email='fastcampus.2016@gmail.com',
            recipient_list=email_list,
        )
        return Response(status=status.HTTP_200_OK)
