# ADVERT
from django.conf.urls import url

from myturkishiid.Views import AdvertViews, FeatureViews, CategoryViews, CityViews

app_name = 'myturkishid'

urlpatterns = [

    # advert url
    url(r'advert-save/$', AdvertViews.advert_save, name='advert-save'),
    url(r'get-adverts/$', AdvertViews.get_adverts, name='get-advert'),
    url(r'get-advert-feature/(?P<pk>\d+)$', FeatureViews.get_featureType_advert, name='get-advert-featureType'),
    url(r'add-features-to-advert/(?P<advert_id>\d+)$', AdvertViews.add_feature_to_advert,
        name='add-features-to-advert'),
    url(r'advertDesc-save/(?P<pk>\d+)$', AdvertViews.AdvertDesc_save, name='advertDesc-save'),
    url(r'delete-features-from-advert/(?P<feature_id>\d+)/(?P<advert_id>\d+)$', AdvertViews.delete_feature_from_advert,
        name='delete-features-from-advert'),

    # feaute url
    url(r'feature-save/$', FeatureViews.feature_save, name='feature-save'),
    # url(r'feature-type-save/(?P<pk>\d+)$', FeatureViews.featureType_feature_save, name='feature-type-save'),
    url(r'featureDesc-save/(?P<pk>\d+)$', FeatureViews.featureDesc_save, name='featureDesc-save'),
    url(r'get-feature/$', FeatureViews.get_feature, name='get-feature'),
    url(r'featureType-save/$', FeatureViews.featureType_save, name='featureType-save'),
    url(r'featureTypeDesc-save/(?P<pk>\d+)$', FeatureViews.featureTypeDesc_save, name='featureTypeDesc-save'),
    url(r'add-features-to-feature-type/(?P<featuretype_id>\d+)$', FeatureViews.add_feature_to_feature_type,
        name='add-features-to-feature-type'),
    url(r'delete-features-from-feature-type/(?P<feature_id>\d+)$', FeatureViews.delete_feature_from_feature_type,
        name='delete-features-from-feature-type'),
    url(r'feature-type/$', FeatureViews.feature_type, name='feature-type'),

    # category url
    url(r'category-save/$', CategoryViews.category_save, name='category-save'),
    url(r'categoryDesc-save/(?P<pk>\d+)$', CategoryViews.categoryDesc_save, name='categoryDesc-save'),
    url(r'get-category/$', CategoryViews.get_category, name='get-category'),

    url(r'ilce-getir/$', CityViews.get_districts, name="advert-ilce-getir"),

]
