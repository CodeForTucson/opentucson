# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Crime.weapon1desc'
        db.alter_column(u'crime_crime', 'weapon1desc', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.inci_id'
        db.alter_column(u'crime_crime', 'inci_id', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.report_date'
        db.alter_column(u'crime_crime', 'report_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Crime.hour_rept'
        db.alter_column(u'crime_crime', 'hour_rept', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.offense'
        db.alter_column(u'crime_crime', 'offense', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.add_dir_ns'
        db.alter_column(u'crime_crime', 'add_dir_ns', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.add_dir_ew'
        db.alter_column(u'crime_crime', 'add_dir_ew', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.ycoord'
        db.alter_column(u'crime_crime', 'ycoord', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Crime.add_ns'
        db.alter_column(u'crime_crime', 'add_ns', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.addr_100_blk'
        db.alter_column(u'crime_crime', 'addr_100_blk', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.start_date'
        db.alter_column(u'crime_crime', 'start_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Crime.end_date'
        db.alter_column(u'crime_crime', 'end_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Crime.plat'
        db.alter_column(u'crime_crime', 'plat', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.date_rept'
        db.alter_column(u'crime_crime', 'date_rept', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.date_occu'
        db.alter_column(u'crime_crime', 'date_occu', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.xcoord'
        db.alter_column(u'crime_crime', 'xcoord', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Crime.neighborhd'
        db.alter_column(u'crime_crime', 'neighborhd', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.date_fnd'
        db.alter_column(u'crime_crime', 'date_fnd', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.weapon2desc'
        db.alter_column(u'crime_crime', 'weapon2desc', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.add_ew'
        db.alter_column(u'crime_crime', 'add_ew', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.naturecode'
        db.alter_column(u'crime_crime', 'naturecode', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.hour_occu'
        db.alter_column(u'crime_crime', 'hour_occu', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.hour_fnd'
        db.alter_column(u'crime_crime', 'hour_fnd', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.howreceive'
        db.alter_column(u'crime_crime', 'howreceive', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Crime.csdisposit'
        db.alter_column(u'crime_crime', 'csdisposit', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Crime.weapon1desc'
        raise RuntimeError("Cannot reverse this migration. 'Crime.weapon1desc' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.inci_id'
        raise RuntimeError("Cannot reverse this migration. 'Crime.inci_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.report_date'
        raise RuntimeError("Cannot reverse this migration. 'Crime.report_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.hour_rept'
        raise RuntimeError("Cannot reverse this migration. 'Crime.hour_rept' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.offense'
        raise RuntimeError("Cannot reverse this migration. 'Crime.offense' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.add_dir_ns'
        raise RuntimeError("Cannot reverse this migration. 'Crime.add_dir_ns' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.add_dir_ew'
        raise RuntimeError("Cannot reverse this migration. 'Crime.add_dir_ew' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.ycoord'
        raise RuntimeError("Cannot reverse this migration. 'Crime.ycoord' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.add_ns'
        raise RuntimeError("Cannot reverse this migration. 'Crime.add_ns' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.addr_100_blk'
        raise RuntimeError("Cannot reverse this migration. 'Crime.addr_100_blk' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.start_date'
        raise RuntimeError("Cannot reverse this migration. 'Crime.start_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.end_date'
        raise RuntimeError("Cannot reverse this migration. 'Crime.end_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.plat'
        raise RuntimeError("Cannot reverse this migration. 'Crime.plat' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.date_rept'
        raise RuntimeError("Cannot reverse this migration. 'Crime.date_rept' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.date_occu'
        raise RuntimeError("Cannot reverse this migration. 'Crime.date_occu' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.xcoord'
        raise RuntimeError("Cannot reverse this migration. 'Crime.xcoord' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.neighborhd'
        raise RuntimeError("Cannot reverse this migration. 'Crime.neighborhd' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.date_fnd'
        raise RuntimeError("Cannot reverse this migration. 'Crime.date_fnd' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.weapon2desc'
        raise RuntimeError("Cannot reverse this migration. 'Crime.weapon2desc' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.add_ew'
        raise RuntimeError("Cannot reverse this migration. 'Crime.add_ew' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.naturecode'
        raise RuntimeError("Cannot reverse this migration. 'Crime.naturecode' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.hour_occu'
        raise RuntimeError("Cannot reverse this migration. 'Crime.hour_occu' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.hour_fnd'
        raise RuntimeError("Cannot reverse this migration. 'Crime.hour_fnd' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.howreceive'
        raise RuntimeError("Cannot reverse this migration. 'Crime.howreceive' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Crime.csdisposit'
        raise RuntimeError("Cannot reverse this migration. 'Crime.csdisposit' and its values cannot be restored.")

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