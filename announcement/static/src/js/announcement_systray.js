/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { ScheduledActionsTemplate } from './scheduled_actions';

const { mount } = owl;
class AnnouncementSystray extends owl.Component {

    setup() {
        this.action = useService("action");
    }

    //    Click of the systray
    _onClickScheduledAction() {

        if ($(".botIcon").length == 0) {
            this.schedule_dropdown = mount(ScheduledActionsTemplate, document.body)

        } else if ($(".botIcon").length > 0) {
            this.schedule_dropdown.then(function(res) {
                res.__owl__.remove()
            })
        }


    }

}
ScheduledActions.template = "AnnouncementSystray";

export const systrayItem = {
    Component: AnnouncementSystray
};

registry.category("systray")
    .add("AnnouncementSystray", systrayItem, {
        sequence: 1
    });

///** @odoo-module **/
//import SystrayMenu from 'web.SystrayMenu';
//import Widget from 'web.Widget';
//var PurchaseOrder = Widget.extend({
//  template: 'weather_wizard_template',
//  events: {
////      'click #create_order': '_onClick',
//  },
////  _onClick: function(){
////      this.do_action({
////           type: 'ir.actions.act_window',
////           name: 'Purchase Order',
////           res_model: 'sale.order',
////           view_mode: 'form',
////           views: [[false, 'form']],
////           target: 'new'
////      });
////  },
//});
//SystrayMenu.Items.push(PurchaseOrder);
//export default PurchaseOrder;