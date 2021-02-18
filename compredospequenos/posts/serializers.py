# Third party imports.
from rest_framework import serializers

# Local application imports
from .models import Post
from accounts.models import CustomUser
User = CustomUser




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','last_login','email','firstName','lastName','gender', 'birthDate', 'bio',
'image','joinedAt', 'updatedAt',)
class PostSerializer(serializers.ModelSerializer):
    username = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['username']
                  