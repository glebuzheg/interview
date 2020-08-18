from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import VoteQuestion, VoteVariant, VoteAnswer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class VoteVariantSerializer(serializers.ModelSerializer):
    answers_count = serializers.SerializerMethodField(read_only=True)
    answers_percent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = VoteVariant
        fields = (
            'id',
            'description',
            'answers_count',
            'answers_percent',
        )

    def get_answers_count(self, obj):
        return obj.answers.count()

    def get_answers_percent(self, obj):
        a_count = obj.answers.count()
        if a_count:
            return a_count * 100 / obj.question.answers.count()
        return 0


class VoteQuestionSerializer(serializers.ModelSerializer):
    variants = VoteVariantSerializer(many=True)

    class Meta:
        model = VoteQuestion
        fields = (
            'id',
            'start_date',
            'end_date',
            'title',
            'v_type',
            'variants'
        )


class VoteAnswerSerializer(serializers.ModelSerializer):
    variants = serializers.PrimaryKeyRelatedField(queryset=VoteVariant.objects.all(), many=True, allow_null=True)

    class Meta:
        model = VoteAnswer
        fields = [
            'id',
            'variants',
            'question',
            'value',
            'user',
            'created_at'
        ]
        extra_kwargs = {
            'question': {'required': True},
        }
        read_only_fields = (
            'id',
            'created_at'
        )

    def validate_question(self, question):
        if not question.is_active:
            raise serializers.ValidationError('Опрос еще не начался или завершон')
        return question

    def validate(self, attrs):
        question = attrs.get('question')
        variants = attrs.get('variants', [])
        q_variants = question.variants.all()
        q_v_type = question.v_type
        # check correct values
        if q_v_type != VoteQuestion.TEXT:
            if not all(v in q_variants for v in variants):
                raise serializers.ValidationError('Выбирите правильный вариант из этого опроса')
            attrs.pop('value', None)
            if q_v_type == VoteQuestion.SINGLE and len(variants) > 1:
                raise serializers.ValidationError('Необходимо указать 1 вариант ответа')

        else:
            attrs.pop('variants', [])
            if not attrs.get('value'):
                raise serializers.ValidationError({
                    'value': f"При типе вопроса {q_v_type} необходимо указать комментарий"
                })

        return attrs

    def create(self, validated_data):
        return super().create(validated_data)


class VoteAnswerListSerializer(VoteAnswerSerializer):
    user = UserSerializer(read_only=True)


class UserAnswerListSerializer(VoteAnswerSerializer):
    question = VoteQuestionSerializer(read_only=True)
