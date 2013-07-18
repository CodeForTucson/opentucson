Crimemap.IndexView = Ember.View.extend({
    classNames: ['map-view'],
    elementId: 'map',
    map: null,

    didInsertElement: function() {
        this._super();

        this.loadMaps();
        this.$().height(document.height-100);
    },

    loadData: function() {
        var points = window.points = Crimemap.Crime.find();
        points.forEach(function(item, index) {
            console.log(item.ycoord);
        });
    },

    initiateMaps: function() {
        var mapOptions = {
            zoom: 13,
            center: new google.maps.LatLng(32.221667, -110.926389),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(this.$().get(0), mapOptions);
        this.set('map', map);
        this.loadData();
    },

    loadMaps: function() {
        var self = this;
        window.map_callback = function() {
            self.initiateMaps();
        };

        $.getScript( 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&callback=map_callback' );
    },

});
