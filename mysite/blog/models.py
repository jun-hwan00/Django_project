from django.db import models
from django.utils import timezone
from django.conf import settings # Django의 User 모델을 가져오기 위함

class Post(models.Model):
    # author 필드 추가: Django의 User 모델과 연결되는 외래 키
    # settings.AUTH_USER_MODEL은 현재 프로젝트에서 사용 중인 User 모델을 가리킵니다.
    # on_delete=models.CASCADE는 연결된 User가 삭제되면 Post도 함께 삭제됨을 의미합니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    # content 대신 text 필드 사용 (안드로이드 앱에서 'text'로 보내므로)
    text = models.TextField() 
    
    # created_at 대신 created_date 필드 사용 (안드로이드 앱에서 'created_date'로 보내므로)
    # default=timezone.now는 객체 생성 시 현재 시간으로 자동 설정합니다.
    created_date = models.DateTimeField(default=timezone.now) 
    
    # published_date 필드 추가 (null=True는 필수가 아님을 의미)
    published_date = models.DateTimeField(blank=True, null=True) 
    
    # 이미지 필드는 그대로 유지
    image = models.ImageField(upload_to = 'intruder_image/%Y/%m/%d/',null=True, blank=True)
    
    def publish(self):
        self.published_date = timezone.now() # time 대신 timezone 사용
        self.save()
    
    def __str__(self):
        return self.title