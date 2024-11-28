from rest_framework import serializers
from .models import MembershipPlans, Member, Trainer, CheckIns, MemberTrainerMapping

class MembershipPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlans
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    membership_type = MembershipPlansSerializer()  # Nested representation of membership plan

    class Meta:
        model = Member
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class CheckInsSerializer(serializers.ModelSerializer):
    member = MemberSerializer()  # Nested representation of member

    class Meta:
        model = CheckIns
        fields = '__all__'

class MemberTrainerMappingSerializer(serializers.ModelSerializer):
    member = MemberSerializer()  # Nested representation of member
    trainer = TrainerSerializer()  # Nested representation of trainer

    class Meta:
        model = MemberTrainerMapping
        fields = '__all__'
