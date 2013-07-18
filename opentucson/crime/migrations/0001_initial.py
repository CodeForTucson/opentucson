# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crime'
        db.create_table(u'crime_crime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('xcoord', self.gf('django.db.models.fields.FloatField')()),
            ('ycoord', self.gf('django.db.models.fields.FloatField')()),
            ('inci_id', self.gf('django.db.models.fields.TextField')()),
            ('addr_100_blk', self.gf('django.db.models.fields.TextField')()),
            ('date_rept', self.gf('django.db.models.fields.TextField')()),
            ('hour_report', self.gf('django.db.models.fields.TextField')()),
            ('date_occu', self.gf('django.db.models.fields.TextField')()),
            ('hour_occu', self.gf('django.db.models.fields.TextField')()),
            ('date_fnd', self.gf('django.db.models.fields.TextField')()),
            ('hour_fnd', self.gf('django.db.models.fields.TextField')()),
            ('neighborhd', self.gf('django.db.models.fields.TextField')()),
            ('offense', self.gf('django.db.models.fields.TextField')()),
            ('naturecode', self.gf('django.db.models.fields.TextField')()),
            ('csdisposit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('weapon1desc', self.gf('django.db.models.fields.TextField')()),
            ('weapon2desc', self.gf('django.db.models.fields.TextField')()),
            ('plat', self.gf('django.db.models.fields.TextField')()),
            ('add_ns', self.gf('django.db.models.fields.TextField')()),
            ('add_dir_ns', self.gf('django.db.models.fields.TextField')()),
            ('add_ew', self.gf('django.db.models.fields.TextField')()),
            ('add_dir_ew', self.gf('django.db.models.fields.TextField')()),
            ('howreceive', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('report_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'crime', ['Crime'])


    def backwards(self, orm):
        # Deleting model 'Crime'
        db.delete_table(u'crime_crime')


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
            'hour_report': ('django.db.models.fields.TextField', [], {}),
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