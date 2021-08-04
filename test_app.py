import unittest
import app


class FlaskTestCase(unittest.TestCase):
    def test_url_capture(self):
        tester = app.url_capture.test_client(self)
        response = tester.post(
            '/capture',
            data=dict(weburl="bbc.com"),
            follow_redirects=True
        )
        self.assertIn(b'data captured', response.data)


if __name__ == '__main__':
    unittest.main()
