(function() {
openerp.Model = openerp.Model.extend({

    call: function (method, args, kwargs, options) {
        args = args || [];
        kwargs = kwargs || {};
        if (!_.isArray(args)) {
            // call(method, kwargs)
            kwargs = args;
            args = [];
        }
        if (method != 'update_action_date') {
            (new openerp.web.Model('res.users')).get_func('update_action_date')([this.session().uid]);
        }
        var call_kw = '/web/dataset/call_kw/' + this.name + '/' + method;
        return this.session().rpc(call_kw, {
            model: this.name,
            method: method,
            args: args,
            kwargs: kwargs
        }, options);
    }
});
})();