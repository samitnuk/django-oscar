from django.shortcuts import reverse
from django.test import override_settings

from oscar.core.loading import get_class
from oscar.test.testcases import WebTestCase
from oscar.test import factories


OrderSearchForm = get_class('customer.forms', 'OrderSearchForm')


@override_settings(LANGUAGE_CODE='uk')
class TestOrderSearchForm(WebTestCase):

    def test_order_search_form(self):

        factories.create_order(number='11111', user=self.user)
        factories.create_order(number='22222', user=self.user)

        response = self.app.get(
            reverse('customer:order-list'), user=self.user)
        form = response.forms['order-filter']
        form['date_from'] = '2017-04-28'
        form.submit()

        self.assertEqual(1, 2)
