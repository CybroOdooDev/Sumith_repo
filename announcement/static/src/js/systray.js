/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
var AnnouncementSystray = Widget.extend({
  template: 'AnnouncementSystray',
  events: {
      'click #create_order': '_onClick',
  },
  _onClick: function(){

  },
});
SystrayMenu.Items.push(AnnouncementSystray);
export default AnnouncementSystray;
