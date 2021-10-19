from rest_framework import serializers

from home.models import Person


class PersonSerializer(serializers.ModelSerializer):
    car = serializers.SlugRelatedField(read_only=True, slug_field='year')

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email', 'car')
        extra_kwargs = {
            'email': {'write_only': True}
        }

    def validate_name(self, value):
        if value == 'admin':
            raise serializers.ValidationError('name can not be admin')
        return value

