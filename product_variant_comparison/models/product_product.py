from odoo import fields, models


class ProductProduct(models.Model):
    """
    This class extends the default Odoo 'product.product' model to add a one-to-many
    relationship with 'variant.attribute' model.
    """
    _inherit = 'product.product'

    attrib_value_ids = fields.One2many('variant.attribute', 'product_id',
                                       help="The list of variant attributes "
                                            "for this product.")


class ProductVariant(models.Model):
    """
    This model represents a variant attribute for a product in Odoo. It is associated
    with a 'product.product' model and can have multiple values defined by 'product.attribute.value'.
    """
    _name = 'variant.attribute'
    product_id = fields.Many2one('product.product',
                                 help="The product this variant attribute "
                                      "belongs to.")
    attribute_id = fields.Many2one('product.attribute', string="Attribute",
                                   help="The attribute associated with this "
                                        "variant.")
    value_id = fields.Many2one('product.attribute.value', string='Values',
                               domain="[('attribute_id','=',attribute_id)]",
                               help="The possible values for this variant "
                                    "attribute.")
