from rest_framework import serializers
from .models import User

import re

class RegisterSerializer(serializers.ModelSerializer):

    identifier=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["username","identifier","phone_number","password"]

        extra_kwargs={'password':{'write_only':True}}
    


    def validate(self,data):
        if "@" in data["identifier"]:
            #this is how we can use the drf's builtin validator in differnt places
            validate_email=serializers.EmailField()
            data["email"]=validate_email.run_validation(data["identifier"])

        else:
            if not re.fullmatch(r'[6-9][0-9]{9}', data["identifier"]):
                raise serializers.ValidationError("Enter a valid email or 10-digit phone number.")

            data["phone_number"] = data['identifier']

        return data

    def create(self,data):

        data.pop("identifier")

        password=data.pop("password")

        #**data means unpck the dict to variable and value for storing in table
        user=User(**data)

        user.set_password(password)

        user.save()

        return user






            
             


    