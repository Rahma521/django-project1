from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def testHomePageStatusCode(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def testAboutPageStatusCode(self):
        response = self.client.get("about/")
        self.assertEqual(response.status_code, 200)