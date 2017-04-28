from django.shortcuts import reverse
from django.test import override_settings

from oscar.core.loading import get_class
from oscar.test.testcases import WebTestCase
from oscar.test import factories


OrderSearchForm = get_class('customer.forms', 'OrderSearchForm')


@override_settings(LANGUAGE_CODE='pl')
class TestOrderSearchForm(WebTestCase):

    def test_order_search_form(self):

        order1 = factories.create_order(number='11111')
        order2 = factories.create_order(number='22222')

        form = self.app.get(
            reverse('customer:order-list'), user=self.user
        )
        # form['date_from'] = '2017-04-15'
        # form.submit()

        print(form)
        self.assertEqual(1, 2)
