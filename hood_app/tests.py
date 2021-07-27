from django.test import TestCase
from .models import Profile, Post, Business, Neighbourhood
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='tajeu',email='tajeusanta7@gmail.com', password='1234567890')
        self.user.save()



class TestNeigbourhood(TestCase):
    def setUp(self):
        self.Neighbourhood = Neigbourhood(name='Jimcy', description='Living is for the living', location='Ngummoi',admin='santa' , police_number=911, healthcenter_number=911, occupants_count='5')
        self.Neighbourhood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Neighbourhood, Neigbourhood))



class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(username='santaskye', email='tajeusanta7@gmail.com', password='1234567')
        self.user.save()

        self.busines = Business(name='Gift shop', email='tajeusanta7@gmail.com', description='Living is for the living', neighbourhood=self.hood, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.busins, Business))

    def test_save_hood(self):
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_hood(self):
        business = Business.objects.all().delete()
        self.assertTrue(len(business) > 0)
