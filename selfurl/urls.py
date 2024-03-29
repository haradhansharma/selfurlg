
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


'''
=====
DO NOT FORGET TO MAKE MIGRATION AFTER ADDING PATH! IT IS IMPORTNT!
=====
'''

app_name = 'selfurl'


sitemaps = {
    'static': SelfurlSitemap,
    # 'experiencesitemap': UserSitemap,   
    # 'logssitemap' : UrlLogsSitemap,
    # 'urlsitemap' : UrlSitemap,
    
}


urlpatterns = [
    path('', views.index, name='index'),    
    path('report-malicious/', views.report_malicious, name='report_malicious'),
    path('statistics/', views.statistics, name='statistics'),    
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),   
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robot'),
] 

def get_self_urls():        
        url_list = []
        
        for url in urlpatterns: 
            #skipping url with arguments                 
            c = [url for i in str(url.pattern ).split('/')  if i.startswith('<')  ]             
            if url not in c :         
                path_name = (
                str(app_name + ':' + url.name) , str(url.name.capitalize())  ,          
                )
                url_list.append(path_name)        
                 
        return url_list 
    
urlpatterns += [
    path('<str:short_url>', views.redirect_url, name='redirect_url'),
    path('logs/<str:short_url>', views.log_details, name='log_details'),
    path('allreport/<str:short_url>', views.allreport, name='allreport'),
]  

