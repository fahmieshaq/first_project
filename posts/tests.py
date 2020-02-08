from .models import Post
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testusername = get_user_model().objects.create_user(
            username='testuser', email='testuser@gmail.com',
        )

        Post.objects.create(
            title='Test Post 1', desc='Post 1 desc', author=testusername,
        )

    def test_get_post_detail_from_model(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.title}', 'Test Post 1')
        self.assertEqual(f'{post.desc}', 'Post 1 desc')
        self.assertEqual(f'{post.author}', 'testuser')

    def test_ping_post_list_api(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_ping_post_detail_api(self):
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_valid_post_detail_api(self):
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.content, b'{"id":1,"title":"Test Post 1","desc":"Post 1 desc"}')

    def test_get_invalid_post_detail_api(self):
        response = self.client.get(reverse('posts_detail', kwargs={'pk': 2}))
        self.assertEqual(response.content, b'{"detail":"Not found."}')
