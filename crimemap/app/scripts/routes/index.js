Crimemap.IndexRoute = Ember.Route.extend({
    model: function() {
        return Crimemap.Crime.find();
    }
});
