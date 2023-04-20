from odoo import http
from odoo.http import request


class VariantCompare(http.Controller):
    """Controller for the variant comparison feature in the website product page.

    This controller defines a route to handle the comparison of multiple product variants
    selected by the user. It expects a list of product variant IDs as a parameter in the URL.
    """

    @http.route(['/variant/compare/<dat>'], type='http', auth='public',
                website=True)
    def compare_variant(self, dat):
        """Renders the comparison template and passes the necessary values.
        """
        data = []
        for num in dat.split(','):
            data.append(int(num))
        product_bread = request.env['product.template'].browse(data[-1])
        data.pop()
        variants = request.env['product.product'].browse(data)
        values = {
            'variants': variants,
            'product_bread': product_bread
        }
        return request.render('product_variant_comparison.variant_compare', values)