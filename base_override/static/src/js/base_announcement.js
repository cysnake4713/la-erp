openerp.base_override = function (instance) {

    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.web.WebClient.include({
        show_application: function () {
            return $.when(this._super.apply(this, arguments)).then(this.proxy('show_annoucement_bar'));
        },
        _ab_location: function (dbuuid) {
            return _.str.sprintf('https://services.openerp.com/openerp-enterprise/ab/css/%s.css', dbuuid);
        },
        show_annoucement_bar: function () {
        }
    });
};