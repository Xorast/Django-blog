from django.urls    import path
from .views         import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('<pk>/', post_detail, name='post_detail'),
    path('<pk>/edit', create_or_edit_post, name='edit_detail'),
    path('', get_posts, name='get_posts'),
]