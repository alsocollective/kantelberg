# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field cover_image on 'Project'
        m2m_table_name = db.shorten_name(u'product_project_cover_image')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'product.project'], null=False)),
            ('image', models.ForeignKey(orm[u'media_library.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'image_id'])


    def backwards(self, orm):
        # Removing M2M table for field cover_image on 'Project'
        db.delete_table(db.shorten_name(u'product_project_cover_image'))


    models = {
        u'media_library.image': {
            'Meta': {'object_name': 'Image'},
            'carousel': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'product.about': {
            'Meta': {'object_name': 'About'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'company_info': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'company_info_title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_lag': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'map_info_bubble': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'media_press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'about-media+'", 'symmetrical': 'False', 'to': u"orm['product.Press']"}),
            'media_title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'services_one_description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'services_one_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services_one_image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'services_one_title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'services_title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'services_two_description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'services_two_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services_two_image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'services_two_title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'team_one_description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'team_one_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_one_image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'team_one_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'team_three_description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'team_three_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_three_image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'team_three_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'team_title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'team_two_description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'team_two_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_two_image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'team_two_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'product.press': {
            'Meta': {'object_name': 'Press'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'press-images+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'product.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'product-shots+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'price': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'specification': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'whats_new': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'whats_new_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'product.productcat': {
            'Meta': {'object_name': 'ProductCat'},
            'cover_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cover-image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'products+'", 'symmetrical': 'False', 'to': u"orm['product.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        u'product.project': {
            'Meta': {'object_name': 'Project'},
            'cover_image': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project-cover-image+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project-images+'", 'symmetrical': 'False', 'to': u"orm['media_library.Image']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        }
    }

    complete_apps = ['product']