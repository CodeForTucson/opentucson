# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Crime.neighborhood'
        db.alter_column(u'crime_crime', 'neighborhood_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crime.Neighborhood'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Crime.neighborhood'
        raise RuntimeError("Cannot reverse this migration. 'Crime.neighborhood' and its values cannot be restored.")

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
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'", 'srid': '102649', 'null': 'True', 'blank': 'True'}),
            'naturecode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neighborhd': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crime.Neighborhood']", 'null': 'True', 'blank': 'True'}),
            'offense': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plat': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'weapon1desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'weapon2desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'xcoord': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ycoord': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crime.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '102649'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '38'}),
            'ward': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['crime']