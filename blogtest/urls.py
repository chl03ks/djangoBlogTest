from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blogtest.views.index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', 'blogtest.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', 'blogtest.views.view_category', name='view_blog_category'),
]
