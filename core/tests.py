import datetime
from django.urls import reverse
from django.test import TestCase

from core.models import Leave, Staff

# Create your tests here.

class LeaveRequestTest(TestCase):
    def setUp(self):
        # Create two staff users
        test_staff1 = Staff.objects.create(first_name='testuser1',last_name='testuser1l',email='testuser1@test.com' )
        test_staff2 = Staff.objects.create(first_name='testuser2',last_name='testuser2l',email='testuser2@test.com' )

        test_staff1.save()
        test_staff2.save()

    
        test_leave = Leave.objects.create(staff=test_staff1, start_date = datetime.date(2022, 4, 7), end_date = datetime.date(2022, 4, 10))

    def test_list_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_request_list.html')

    def test_leave_string_method(self):
        leave = Leave.objects.get(id=1)
        expected_string = f'Leave request for {leave.staff.first_name} {leave.staff.last_name} from {leave.start_date} to {leave.end_date}'
        self.assertEqual(str(leave), expected_string)
