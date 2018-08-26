from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Songs
from ..serializer import SongSerializer


# test for views

class BaseViewTestCase(APITestCase):
    client = APIClient()
    print(client)

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)


    def setUp(self):

        self.create_song(title='One Girl', artist='Quantum')
        self.create_song(title='Programmers', artist='Leah')
        self.create_song(title='Happy Birthday', artist='Jayden')
        self.create_song(title='Hacking', artist='Gilberto')


class GetAllSongs(BaseViewTestCase):

    def test_get_all_songs(self):
        
        response = self.client.get(
                    reverse('songs-all')
                )
        expected = Songs.objects.all()
        serialized = SongSerializer(expected, many=True)
        self.assertEqual(serialized.data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)


