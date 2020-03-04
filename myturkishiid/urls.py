# ADVERT
from django.conf.urls import url
from django.urls import path

from myturkishiid.Views import AdvertViews, FeatureViews, CategoryViews, CityViews, HomeViews, UserViews

app_name = 'myturkishid'

urlpatterns = [

    # advert url
    url(r'advert-save/$', AdvertViews.advert_save, name='advert-save'),
    url(r'get-adverts/$', AdvertViews.get_adverts, name='get-advert'),
    url(r'add-features-to-advert/(?P<advert_id>\d+)$', AdvertViews.add_feature_to_advert,
        name='add-features-to-advert'),
    url(r'advertDesc-save/(?P<pk>\d+)$', AdvertViews.AdvertDesc_save, name='advertDesc-save'),
    url(r'delete-features-from-advert/(?P<feature_id>\d+)/(?P<advert_id>\d+)$', AdvertViews.delete_feature_from_advert,
        name='delete-features-from-advert'),
    url(r'advert-update/(?P<pk>\d+)$', AdvertViews.advert_update, name='advert-update'),
    url(r'advert-image-delete/$', AdvertViews.advert_image_delete, name='advert-image-delete'),
    url(r'advert-delete-titleDesc/(?P<advert_id>\d+)/(?P<advertDesc_id>\d+)$', AdvertViews.delete_advertDesc,
        name='delete-advertDesc'),
    url(r'advertDesc-update/(?P<pk>\d+)$', AdvertViews.advertDesc_update, name='advertDesc-update'),
    url(r'advert-delete/$', AdvertViews.advert_delete, name='delete-advert'),

    # feaute url
    url(r'feature-save/$', FeatureViews.feature_save, name='feature-save'),
    # url(r'feature-type-save/(?P<pk>\d+)$', FeatureViews.featureType_feature_save, name='feature-type-save'),
    url(r'feature-type-desc-update/(?P<pk>\d+)$', FeatureViews.featureType_desc_update,
        name='feature-type-desc-update'),
    url(r'feature-desc-update/(?P<pk>\d+)$', FeatureViews.feature_desc_update,
        name='feature-desc-update'),
    url(r'featureDesc-save/(?P<pk>\d+)$', FeatureViews.featureDesc_save, name='featureDesc-save'),
    url(r'get-feature/$', FeatureViews.get_feature, name='get-feature'),
    url(r'featureType-save/$', FeatureViews.featureType_save, name='featureType-save'),
    url(r'featureTypeDesc-save/(?P<pk>\d+)$', FeatureViews.featureTypeDesc_save, name='featureTypeDesc-save'),
    url(r'add-features-to-feature-type/(?P<featuretype_id>\d+)$', FeatureViews.add_feature_to_feature_type,
        name='add-features-to-feature-type'),
    url(r'delete-features-from-feature-type/(?P<feature_id>\d+)$', FeatureViews.delete_feature_from_feature_type,
        name='delete-features-from-feature-type'),
    url(r'feature-type/$', FeatureViews.feature_type, name='feature-type'),
    url(r'feature-delete/(?P<feature_id>\d+)$', FeatureViews.feature_delete, name='feature-delete'),

    # category url
    url(r'category-save/$', CategoryViews.category_save, name='category-save'),
    url(r'categoryDesc-save/(?P<pk>\d+)$', CategoryViews.categoryDesc_save, name='categoryDesc-save'),
    url(r'categoryDesc-update/(?P<pk>\d+)$', CategoryViews.categoryDesc_update, name='categoryDesc-update'),
    url(r'get-category/$', CategoryViews.get_category, name='get-category'),
    url(r'category-delete/(?P<category_id>\d+)$', CategoryViews.category_delete, name='category-delete'),

    url(r'ilce-getir/$', CityViews.get_districts, name="advert-ilce-getir"),

    # home
    # url(r'/', HomeViews.index, name='home'),
    path('', HomeViews.index, name='home'),
    url(r'home/advert-detail/(?P<pk>\d+)$', HomeViews.get_advert, name='advert-detail'),

    # cookie
    url(r'set-lang/(?P<pk>\d+)$', HomeViews.setcookie, name='set-lang'),

    # Kullanıcı

    url(r'add-user/$', UserViews.return_add_users, name='kullanici-ekle'),
    url(r'users/$', UserViews.return_my_users, name='uyelerim'),
    url(r'user-update/(?P<pk>\d+)$', UserViews.users_update, name='uye-guncelle'),
    url(r'user-delete/(?P<pk>\d+)$', UserViews.user_delete, name='uye-sil'),

]
