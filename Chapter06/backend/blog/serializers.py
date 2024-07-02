from rest_framework import serializers
from rest_framework import validators

from blog import models
from author import models as author_models


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"


class BlogCustomSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("Custom create method is called")
        return super(BlogCustomSerializer, self).create(validated_data)

    class Meta:
        model = models.Blog
        fields = "__all__"


# ================== ОБНОВЛЕНИЕ СУЩЕСТВУЮЩИХ ОБЪЕКТОВ МОДЕЛИ ================= #


class BlogCustom2Serializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        print("*** Custom Update method ****")
        return super(BlogCustom2Serializer, self).update(instance, validated_data)

    class Meta:
        model = models.Blog
        fields = "__all__"


# ==================== РЕАЛИЗАЦИЯ ОТНОШЕНИЙ СЕРИАЛИЗАТОРА ==================== #


class BlogCustom3Serializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=author_models.Author.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=models.Tags.objects.all(), many=True, allow_empty=True
    )
    cover_image = serializers.PrimaryKeyRelatedField(
        queryset=models.CoverImage.objects.all(),
        validators=[validators.UniqueValidator(models.CoverImage.objects.all())],
    )

    class Meta:
        model = models.Blog
        fields = "__all__"


# ==================== РАБОТА С ВЛОЖЕННЫМИ СЕРИАЛИЗАТОРАМИ =================== #


class BASerializer(serializers.ModelSerializer):
    class Meta:
        model = author_models.Author
        fields = ["name", "bio"]


class BlogCustom4Serializer(serializers.ModelSerializer):
    author_details = BASerializer(source="author")

    class Meta:
        model = models.Blog
        fields = "__all__"


# ====================== ИЗУЧЕНИЕ SERIALIZERMETHODFIELD ====================== #


class BlogCustom5Serializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField()

    def get_word_count(self, obj):
        return len(obj.content.split())

    class Meta:
        model = models.Blog
        fields = "__all__"


# ================= ИСПОЛЬЗОВАТЬ ПОЛЬЗОВАТЕЛЬСКОЕ ИМЯ МЕТОДА ================= #


class BlogCustom6CustomSerializer(serializers.ModelSerializer):
    word_count = serializers.SerializerMethodField(method_name="use_custom_word_count")

    def use_custom_word_count(self, obj):
        return len(obj.content.split())

    class Meta:
        model = models.Blog
        fields = "__all__"


# ===================== НАСТРОЙКА ПРОВЕРКИ НА УРОВНЕ ПОЛЯ ==================== #


class BlogCustom7Serializer(serializers.ModelSerializer):
    def validate_title(self, value):
        print("validate_title method")
        if "_" in value:
            raise serializers.ValidationError("illegal char")
        return value

    class Meta:
        model = models.Blog
        fields = "__all__"


# ========== ОПРЕДЕЛЕНИЕ ПОЛЬЗОВАТЕЛЬСКОГО ВАЛИДАТОРА НА УРОВНЕ ПОЛЯ ========= #


def demo_func_validator(attr):
    print("func val")
    if "_" in attr:
        raise serializers.ValidationError("invalid char")
    return attr


class BlogCustom8Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        extra_kwargs = {
            "title": {"validators": [demo_func_validator]},
            "content": {"validators": [demo_func_validator]},
        }


# =================== ВЫПОЛНЕНИЕ ПРОВЕРКИ НА УРОВНЕ ОБЪЕКТА ================== #


class BlogCustom9Serializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs["title"] == attrs["content"]:
            raise serializers.ValidationError("Title and content cannot have value")
        return attrs

    class Meta:
        model = models.Blog
        fields = "__all__"


# ======== ОПРЕДЕЛЕНИЕ ПОЛЬЗОВАТЕЛЬСКИХ ВАЛИДАТОРОВ НА УРОВНЕ ОБЪЕКТОВ ======= #


def custom_obj_validator(attrs):
    print("custom object validator")
    if attrs["title"] == attrs["content"]:
        raise serializers.ValidationError("Title and content cannot have the same")
    return attrs


class BlogCustom10Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        validators = [custom_obj_validator]


# ======================== ПОРЯДОК ОЦЕНКИ ВАЛИДАТОРОВ ======================== #


def func_validator(attr):  # 1- Evaluates first
    print("func val")
    if "*" in attr:
        raise serializers.ValidationError("Illegal char")
    return attr


class BlogCustom11Serializer(serializers.ModelSerializer):
    def validate_title(self, value):  # 2-If func_validator succeeds
        print("validate_title method")
        if "_" in value:
            raise serializers.ValidationError("Illegal char")
        return value

    def validate(self, attrs):  # 3- If all field validator succeeds
        print("main validate method")
        return attrs

    class Meta:
        model = models.Blog
        fields = "__all__"
        extra_kwargs = {"title": {"validators": [func_validator]}}


# ======= УДАЛЕНИЕ ВАЛИДАТОРОВ ПО УМОЛЧАНИЮ ИЗ КЛАССА СЕРИАЛИЗАТОРА DRF ====== #


class BlogCustom12Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        validators = []


# ====================== ИСПОЛЬЗОВАНИЕ TO_INTERNAL_VALUE ===================== #


class BlogCustom13Serializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        print("before validation", data)
        return super().to_internal_value(data)

    class Meta:
        model = models.Blog
        fields = "__all__"


# ====================== ИСПОЛЬЗОВАНИЕ TO_REPRESENTATION ===================== #


class BlogCustom14Serializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp["title"] = resp["title"].upper()
        return resp

    class Meta:
        model = models.Blog
        fields = "__all__"


# ========= ИСПОЛЬЗОВАНИЕ АРГУМЕНТА КОНТЕКСТА ДЛЯ ПЕРЕДАЧИ ИНФОРМАЦИИ ======== #


class BlogCustom15Serializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        print("Printing context –", self.context)
        return super().to_internal_value(data)

    class Meta:
        model = models.Blog
        fields = "__all__"


# =========== ПЕРЕДАЧА ПОЛЬЗОВАТЕЛЬСКОГО QUERYSET В PRIMARYKEYFIELD ========== #


class CustomPKRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        req = self.context.get("request", None)  # context value
        queryset = super().get_queryset()  # retrieve default filter
        if not req:
            return None
        return queryset.filter(user=req.user)  # additional filter


class BlogCustom16Serialzier(serializers.ModelSerializer):
    tags = CustomPKRelatedField(queryset=models.Tags.objects.all())

    class Meta:
        model = models.Blog
        fields = "__all__"


# ============================================================================ #
