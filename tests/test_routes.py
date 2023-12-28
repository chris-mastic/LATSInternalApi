import unittest

from base_test import BaseTestCase
from flask_login import current_user

class TestIndex(BaseTestCase):
    def test_index_route(self):
        response = self.client.get("/",follow_redirects=True)
        self.assertTrue(response.status_code == 200)

    def test_login_route(self):
        response = self.client.get("/api/login",follow_redirects=True)
        self.assertTrue(response.status_code == 200)

    def test_logout_route(self):
        response = self.client.get("/api/logout",follow_redirects=True)
        self.assertTrue(response.status_code == 200)    

    def test_reset_password_route(self):
        response = self.client.get("/api/reset_password", follow_redirects=True)
        self.assertTrue(response.status_code == 200)

    def test_forgot_password_route(self):
        response = self.client.get("/api/forgot_password", follow_redirects=True)
        self.assertTrue(response.status_code == 200)    

    def test_add_to_batch_route(self):
        response = self.client.get("/api/add_to_batch", follow_redirects=True)
        self.assertTrue(response.status_code == 200)

    def test_get_status_route(self):
        response = self.client.get("/api/get_status", follow_redirects=True)
        self.assertTrue(response.status_code == 200)

    def test_submit_batch_route(self):
        response = self.client.get("/api/submit_batch", follow_redirects=True)
        self.assertTrue(response.status_code == 200)


# class TestPublic(BaseTestCase):
#     def test_main_route_requires_login(self):
#         # Ensure main route requres logged in user.
#         response = self.client.get("/", follow_redirects=True)
#         self.assertTrue(response.status_code == 200)
#         self.assertIn(b"Please log in to access this page", response.data)

#     def test_logout_route_requires_login(self):
#         # Ensure logout route requres logged in user.
#         response = self.client.get("/logout", follow_redirects=True)
#         self.assertIn(b"Please log in to access this page", response.data)


# class TestLoggingInOut(BaseTestCase):
#     def test_correct_login(self):
#         # Ensure login behaves correctly with correct credentials
#         with self.client:
#             response = self.client.post(
#                 "/login",
#                 data=dict(email="ad@min.com", password="admin_user"),
#                 follow_redirects=True,
#             )
#             self.assertTrue(current_user.email == "ad@min.com")
#             self.assertTrue(current_user.is_active)
#             self.assertTrue(response.status_code == 200)

#     def test_logout_behaves_correctly(self):
#         # Ensure logout behaves correctly, regarding the session
#         with self.client:
#             self.client.post(
#                 "/login",
#                 data=dict(email="ad@min.com", password="admin_user"),
#                 follow_redirects=True,
#             )
#             response = self.client.get("/logout", follow_redirects=True)
#             self.assertIn(b"You were logged out.", response.data)
#             self.assertFalse(current_user.is_active)


if __name__ == "__main__":
    unittest.main()