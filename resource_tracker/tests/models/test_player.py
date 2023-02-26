from django.test import TestCase
from resource_tracker.models import Player
from django.contrib.auth import get_user_model


class PlayerTestCase(TestCase):
    def test_can_create_player(self):
        user = get_user_model().objects.create()
        player = Player.objects.create(user=user, name="test name")
        db_player = Player.objects.get(id=player.id)

        self.assertEqual(db_player.name, "test name")