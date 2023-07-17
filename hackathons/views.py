from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Hackathon
from .serializers import HackathonSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def hackathons(request):
    # get list of hackathons:
	if request.method == 'GET':
		hack_list = Hackathon.objects.all()
		serializer = HackathonSerializer(hack_list, many=True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		req_data = request.data
		serializer = HackathonSerializer(data=req_data)

		if not serializer.is_valid():
			return Response({
				"message": "Error in registering the user",
				"error": serializer.errors
			}, status.HTTP_400_BAD_REQUEST)
		
		serializer.save()

		return Response({
			"Message": "Hackathon Created",
			"Data": serializer.data
		}, status.HTTP_201_CREATED)
