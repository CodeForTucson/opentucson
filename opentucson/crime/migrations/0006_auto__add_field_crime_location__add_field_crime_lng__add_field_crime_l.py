# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Crime.location'
        db.add_column(u'crime_crime', 'location',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0.0 0.0)', srid=102249, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crime.lng'
        db.add_column(u'crime_crime', 'lng',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Crime.lat'
        db.add_column(u'crime_crime', 'lat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Crime.location'
        db.delete_column(u'crime_crime', 'location')

        # Deleting field 'Crime.lng'
        db.delete_column(u'crime_crime', 'lng')

        # Deleting field 'Crime.lat'
        db.delete_column(u'crime_crime', 'lat')


    models = {
        u'crime.crime': {
            'Meta': {'object_name': 'Crime'},
            'add_dir_ew': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'add_dir_ns': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'add_ew': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'add_ns': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'addr_100_blk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'csdisposit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'date_fnd': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_occu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_rept': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hour_fnd': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hour_occu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hour_rept': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'howreceive': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inci_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'", 'srid': '102249', 'null': 'True', 'blank': 'True'}),
            'naturecode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neighborhd': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'offense': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plat': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'weapon1desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'weapon2desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'xcoord': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ycoord': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['crime']