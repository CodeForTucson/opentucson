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
            ('xcoord', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ycoord', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('inci_id', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('addr_100_blk', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_rept', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hour_rept', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_occu', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hour_occu', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_fnd', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('hour_fnd', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('neighborhd', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('offense', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('naturecode', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('csdisposit', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('weapon1desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('weapon2desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plat', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_ns', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_dir_ns', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_ew', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('add_dir_ew', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('howreceive', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('report_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(default='POINT(0.0 0.0)', srid=102649, null=True, blank=True)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crime.Neighborhood'])),
        ))
        db.send_create_signal(u'crime', ['Crime'])

        # Adding model 'Neighborhood'
        db.create_table(u'crime_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=38)),
            ('ward', self.gf('django.db.models.fields.FloatField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=102649)),
        ))
        db.send_create_signal(u'crime', ['Neighborhood'])


    def backwards(self, orm):
        # Deleting model 'Crime'
        db.delete_table(u'crime_crime')

        # Deleting model 'Neighborhood'
        db.delete_table(u'crime_neighborhood')


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
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crime.Neighborhood']"}),
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