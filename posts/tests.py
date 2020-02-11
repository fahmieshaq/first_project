from .models import Post
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # cls.client = APIClient() I had to put it in setUp(self)
        customer_username = get_user_model().objects.create_user(
            username='customer_username', email='customer_user@gmail.com', is_staff=False, is_superuser=False,
        )

        staff_username = get_user_model().objects.create_user(
            username='staff_username', email='staff_user@gmail.com', is_staff=True, is_superuser=False,
        )

        superuser_username = get_user_model().objects.create_user(
            username='superuser_username', email='superuser_user@gmail.com', is_staff=True, is_superuser=True,
        )

        Post.objects.create(
            title='Test Post 1', desc='Post 1 desc', author=customer_username,
        )

       #Post.objects.create(
       #     title='Test Post 2', desc='Post 2 desc', author=customer_username,
       # )

    def setUp(self):
        self.client = APIClient()

    def test_get_post_detail_from_model(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.title}', 'Test Post 1')
        self.assertEqual(f'{post.desc}', 'Post 1 desc')
        self.assertEqual(f'{post.author}', 'customer_username')

    # Test list
    def test_ping_post_list_api(self):
        # self.client = APIClient()
        #posts_list = Post.objects.all() # doesn't work
        posts_list = Post.objects.get() # Post.objects.get() how to test a full list. THIS WORK CAUSE WE HAVE ONE RECORD ONLY
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, posts_list)

    def test_ping_post_detail_api(self):
        # self.client = APIClient()
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #### NEXT
    def test_get_valid_post_detail_api(self):
        posts_list = Post.objects.get(id=1)  # how to test a full list. THIS WORK CAUSE WE HAVE ONE RECORD ONLY
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, posts_list)
        """
        #self.client = APIClient()
        posts_detail = Post.objects.get(id=1)
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.content, posts_detail)
        """
"""

    

    def test_create_post_api(self):
        # self.client = APIClient()
        self.post_data = {"id": 2, "title": "Test Post 2", "desc": "Post 2 desc", "author": 1}
        response = self.client.post(reverse('posts_create'), self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        postlist = Post.objects.get(id=2)
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 2}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, postlist)

    def test_update_post_api(self):
        # self.client = APIClient()
        change_post_data = {"id": 1, "title": "Test Post 1 - Edited"}
        response = self.client.patch(reverse('posts_update', kwargs={'pk': 1}), change_post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        postlist = Post.objects.get(id=1)
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, postlist)

    def test_delete_post_api(self):
        # self.client = APIClient()
        response = self.client.delete(reverse('posts_delete', kwargs={'pk': 1}))
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
"""