from rest_framework.serializers import ModelSerializer

from prof.models import ContactUs, AgentProfile, AgentQuery

class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class AgentProfileSerializer(ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'

class AgentQueryCreateSerializer(ModelSerializer):
    class Meta:
        model = AgentQuery
        exclude = ('agent',)

class AgentProfileCreateSerializer(ModelSerializer):
    class Meta:
#<<<<<<< HEAD
        model = AgentQuery
# =======
#         model = AgentProfile
# >>>>>>> ef57d6dfc36652db4fb58388a8d5887316b505f7
#         exclude = ('user',)