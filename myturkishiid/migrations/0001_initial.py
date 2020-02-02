# Generated by Django 2.1.3 on 2020-01-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertNo', models.CharField(blank=True, max_length=256, null=True, verbose_name='İlan Numarası')),
                ('district', models.TextField(verbose_name='İlçe')),
                ('advertTitle', models.CharField(blank=True, max_length=256, null=True, verbose_name='İlan Başlığı')),
                ('floorNumber', models.CharField(blank=True, choices=[('ZEMİN', 'ZEMİN'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('17 ÜZERİ', '17 ÜZERİ')], default='ZEMİN', max_length=256, null=True, verbose_name='kat numarası')),
                ('bathroomNumber', models.CharField(blank=True, choices=[('YOK', 'YOK'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='YOK', max_length=256, null=True, verbose_name='Banyo Sayısı')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Adres')),
                ('room', models.CharField(choices=[('1+1', '1+1'), ('1.5+1', '1.5+1'), ('2+0', '2+0'), ('2+1', '2+1'), ('2.5+1', '2.5+1'), ('2+2', '2+2'), ('3+1', '3+1'), ('3.5+1', '3.5+1'), ('3+2', '3+2'), ('4+1', '4+1'), ('4.5+1', '4.5+1'), ('4+2', '4+2'), ('4+3', '4+3'), ('4+4', '4+4'), ('5+1', '5+1'), ('5+2', '5+2'), ('5+3', '5+3'), ('5+4', '5+4')], default='1+1', max_length=128, verbose_name='Oda sayısı')),
                ('balcony', models.CharField(blank=True, choices=[('1', 'YOK'), ('2', '1'), ('2 ÜZERİ', '2 Üzeri'), ('YOK', '2 Üzeri')], default='2', max_length=256, null=True, verbose_name='balkon sayısı')),
                ('heating', models.CharField(blank=True, choices=[('YOK', 'YOK'), ('SOBA', 'SOBA'), ('DOĞALGAZ SOBASI', 'DOĞALGAZ SOBASI'), ('KAT KALORİFERİ', 'KAT KALORİFERİ'), ('MERKEZİ', 'MERKEZİ'), ('MERKEZİ(PAY ÖLÇER)', 'MERKEZİ(PAY ÖLÇER)')], default='YOK', max_length=256, null=True, verbose_name='Isıtma türü')),
                ('front', models.CharField(blank=True, choices=[('KUZEY', 'KUZEY'), ('GÜNEY', 'GÜNEY'), ('DOĞU', 'DOĞU'), ('BATI', 'BATI'), ('KUZEYBATI', 'KUZEYBATI'), ('KUZEYDOĞU', 'KUZEYDOĞU'), ('GÜNEYBATI', 'GÜNEYBATI'), ('GÜNEYDOĞU', 'GÜNEYDOĞU')], default='KUZEY', max_length=256, null=True, verbose_name='Cephe')),
                ('isShow', models.BooleanField(default=False)),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
                ('modificationDate', models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')),
                ('paidDate', models.DateTimeField(blank=True, null=True, verbose_name='Kayıt Tarihi')),
                ('fieldNet', models.FloatField(blank=True, null=True, verbose_name='Alan Net')),
                ('fieldBrut', models.FloatField(blank=True, null=True, verbose_name='Alan Brüt')),
                ('buildingAge', models.CharField(blank=True, max_length=256, null=True, verbose_name='Bina Yaşı')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Çeviri')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Advert')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertImage', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='İlan Resmi')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=256, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='İlan Kategorisi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Category')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Yaşadığı Şehir')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='', verbose_name='İkon')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Kur Adı')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='İlçe')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.City')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Özellik Adı')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureTypeDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('featureType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.FeatureType')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Dil')),
                ('flag', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Bayrak')),
            ],
        ),
        migrations.AddField(
            model_name='featuretypedesc',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Language'),
        ),
        migrations.AddField(
            model_name='featuredesc',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Language'),
        ),
        migrations.AddField(
            model_name='feature',
            name='featureType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.FeatureType'),
        ),
        migrations.AddField(
            model_name='categorydesc',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Language'),
        ),
        migrations.AddField(
            model_name='advertdesc',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.Language'),
        ),
        migrations.AddField(
            model_name='advert',
            name='advertImage',
            field=models.ManyToManyField(blank=True, to='myturkishiid.AdvertImage', verbose_name='Ürün Resmi'),
        ),
        migrations.AddField(
            model_name='advert',
            name='category',
            field=models.ManyToManyField(blank=True, to='myturkishiid.Category', verbose_name='İlan Kategorisi'),
        ),
        migrations.AddField(
            model_name='advert',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.City', verbose_name='İl'),
        ),
        migrations.AddField(
            model_name='advert',
            name='feature',
            field=models.ManyToManyField(blank=True, to='myturkishiid.Feature'),
        ),
        migrations.AddField(
            model_name='advert',
            name='featureTitle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myturkishiid.FeatureType', verbose_name='Özellilk Başlık'),
        ),
    ]
