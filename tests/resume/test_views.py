from django.shortcuts import reverse
from django.template import loader
from django.test import TestCase
import pytest

from resume.models import about
from resume.models import project
from resume.models import social


class ResumeViewTests(TestCase):
    @pytest.mark.django_db(True)
    def test_index(self):
        about_data = about.About(
            first_name="Foo",
            last_name="Bar",
            place="Fooland",
            contact="foo@bar.com",
            country="FooCountry",
            description="This is a foo description",
        )
        about_data.save()

        social_link = social.Social(
            url="https://foo.bar",
            title="Foo Bar",
            icon="Icon",
        )
        social_link.save()
        socials = social.Social.objects.all()

        project_data = project.Project(
            name="Foo project",
            number="1",
            achieved=True,
            pending=False,
        )
        project_data.save()
        projects = project.Project.objects.all()

        url = reverse("resume:index")
        response = self.client.get(url)

        context = {
            "resume": about_data,
            "socials": socials,
            "projects": {"projects": projects, "progression": 100},
        }

        assert response.status_code == 200
        assert response.content.decode() == loader.render_to_string(
            "resume/index.html", context
        )
