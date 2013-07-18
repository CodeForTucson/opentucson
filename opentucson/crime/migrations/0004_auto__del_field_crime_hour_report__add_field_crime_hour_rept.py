# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Crime.hour_report'
        db.delete_column(u'crime_crime', 'hour_report')

        # Adding field 'Crime.hour_rept'
        db.add_column(u'crime_crime', 'hour_rept',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Crime.hour_report'
        raise RuntimeError("Cannot reverse this migration. 'Crime.hour_report' and its values cannot be restored.")
        # Deleting field 'Crime.hour_rept'
        db.delete_column(u'crime_crime', 'hour_rept')


    models = {
        u'crime.crime': {
            'Meta': {'object_name': 'Crime'},
            'add_dir_ew': ('django.db.models.fields.TextField', [], {}),
            'add_dir_ns': ('django.db.models.fields.TextField', [], {}),
            'add_ew': ('django.db.models.fields.TextField', [], {}),
            'add_ns': ('django.db.models.fields.TextField', [], {}),
            'addr_100_blk': ('django.db.models.fields.TextField', [], {}),
            'csdisposit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'date_fnd': ('django.db.models.fields.TextField', [], {}),
            'date_occu': ('django.db.models.fields.TextField', [], {}),
            'date_rept': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'hour_fnd': ('django.db.models.fields.TextField', [], {}),
            'hour_occu': ('django.db.models.fields.TextField', [], {}),
            'hour_rept': ('django.db.models.fields.TextField', [], {}),
            'howreceive': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inci_id': ('django.db.models.fields.TextField', [], {}),
            'naturecode': ('django.db.models.fields.TextField', [], {}),
            'neighborhd': ('django.db.models.fields.TextField', [], {}),
            'offense': ('django.db.models.fields.TextField', [], {}),
            'plat': ('django.db.models.fields.TextField', [], {}),
            'report_date': ('django.db.models.fields.DateTimeField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'weapon1desc': ('django.db.models.fields.TextField', [], {}),
            'weapon2desc': ('django.db.models.fields.TextField', [], {}),
            'xcoord': ('django.db.models.fields.FloatField', [], {}),
            'ycoord': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['crime']