# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile,Rating


class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="ruth"
        )

        self.profile = Profile(
            bio="Full-stack dev",
            user=user,
            contact="0712437161",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_create_method(self):
        self.profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
class ProjectTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
               username="ruth"
        )

        self.project = Project(
            title="pizza-joint",
            description="This a website for pizza-joint ,were one can make orders for their pizza having to choose the flavour,size and toppings.Also deliveries are done to those who want their orders be delivered or one can just pick up",
            image="image/upload/v1649620861/pdeg4qgd3rkgchlgwu2a.png",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    

    def test_update_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

   
class ProfileTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="test_user"
        )

        self.profile = Profile(
            bio="Test Profile_photo",
            user=user,
            contact="Test Contact",
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_create_method(self):
        self.profile.create_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
class RatingTestClass(TestCase):
    def setUp(self):
        user = User.objects.create(
               username="ruth"
        )

        self.rating = Rating(
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    