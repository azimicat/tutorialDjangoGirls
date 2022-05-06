from django.contrib import admin
from .models import Post as Post_sv

# Postモデルを登録
admin.site.register(Post_sv)
