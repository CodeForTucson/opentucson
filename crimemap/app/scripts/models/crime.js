Crimemap.Crime = Ember.Model.extend({
    xcoord: Ember.attr(Number),
    ycoord: Ember.attr(Number)
});

Crimemap.Crime.adapter = Ember.FixtureAdapter.create();

Crimemap.Crime.FIXTURES = [
    {
        id: 1,
        xcoord: '1016636.62270341',
        ycoord: '451173.20406824'
    }
]
