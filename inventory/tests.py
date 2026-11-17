from django.test import TestCase


class ApiRootTests(TestCase):
    def test_api_root_renders_browsable_api(self):
        response = self.client.get("/api/", HTTP_ACCEPT="text/html")

        self.assertEqual(response.status_code, 200)
