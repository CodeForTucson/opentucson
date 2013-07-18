from django.db import models

"""
XCoored: 993187.06069554;
YCoord: 445491.49606299;
INCI_ID: 1306020028;
ADDR_100_BLK: S 6TH AV & E BROADWAY BL;
DATE_REPT: 2013-06-02 00:00:00;
HOUR_REPT: 0045;
DATE_OCCU: 2013-06-02 00:00:00;
HOUR_OCCU: 0045;
DATE_FND: 2013-06-02 00:00:00;
HOUR_FND: 0045;
NEIGHBORHD: T502;
OFFENSE: NULL;
NATRUECODE: FD;
CSDISPOSIT: I;
WEAPON1DESC: NULL;
WEAPON2DESC: NULL;
PLAT: 5347;
ADD_NS: 0;
ADD_DIR_NS N;
ADD_EW: 100;
ADD_DIR_EW: E;
HOWRECIEVE: OFFICER
"""

optional = {'blank': True, 'null': True}

class Crime(models.Model):
    #: x coordinate of incident
    xcoord = models.FloatField(**optional)
    #: y coordinate of incident
    ycoord = models.FloatField(**optional)
    #: id of incident
    inci_id = models.TextField(**optional)
    #: 100 block radius (code?) of incident reported
    addr_100_blk = models.TextField(**optional)
    #: date incident was reported
    date_rept = models.TextField(**optional)
    #: hour when incident was reported -- military time
    hour_rept = models.TextField(**optional)
    #: date when incident began
    date_occu = models.TextField(**optional)
    #: hour when incident began -- military time
    hour_occu = models.TextField(**optional)
    #: date incident ended
    date_fnd = models.TextField(**optional)
    #: hour incident ended -- military time
    hour_fnd = models.TextField(**optional)
    #: neighborhood code (TPD Division and Sector)
    neighborhd = models.TextField(**optional)
    #: description of offense
    offense = models.TextField(**optional)
    #: event type code
    naturecode = models.TextField(**optional)
    #: call for service dispostion code
    csdisposit = models.CharField(max_length=10, **optional)
    #: weapon description (if any)
    weapon1desc = models.TextField(**optional)
    #: second (?) weapon description
    weapon2desc = models.TextField(**optional)
    #: fire plat number (?)
    plat = models.TextField(**optional)
    #: north / south 100-block address number
    add_ns = models.TextField(**optional)
    #: north / south address direction
    add_dir_ns = models.TextField(**optional)
    #: east / west 100-block address number
    add_ew = models.TextField(**optional)
    #: east / west address direction
    add_dir_ew = models.TextField(**optional)
    #: how the call for service was recieved
    howreceive = models.TextField(**optional)

    # cleaner fields from parsed data
    start_date = models.DateTimeField(**optional)
    report_date = models.DateTimeField(**optional)
    end_date = models.DateTimeField(**optional)

    def __unicode__(self):
        return self.inci_id
