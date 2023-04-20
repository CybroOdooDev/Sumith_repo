from odoo import models

class ProductTemplate(models.Model):
    """
    This class extends the default Odoo 'product.template' model to add a method '_prepare_variant_values'.
    This method prepares the values needed to create a new product variant based on the attribute
    combination passed as parameter.
    """
    _inherit = 'product.template'

    def _prepare_variant_values(self, combination):
        """
        This method takes an attribute combination and returns a dictionary containing the values
        needed to create a new product variant based on the combination.
        """
        self.ensure_one()
        return {
            'product_tmpl_id': self.id,
            'product_template_attribute_value_ids': [(6, 0, combination.ids)],
            'attrib_value_ids': [
                (0, 0, {'attribute_id': comb.attribute_id.id,
                        'value_id': comb.product_attribute_value_id.id}) for
                comb in
                combination],
            'active': self.active
        }
