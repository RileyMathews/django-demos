# Generated by Django 4.1.7 on 2023-02-23 03:28

from django.db import migrations

def migrate_players(apps, schema_editor):
    GameInstance = apps.get_model('resource_tracker', 'GameInstance')
    GamePlayer = apps.get_model('resource_tracker', 'GamePlayer')
    PlayerResourceInstance = apps.get_model('resource_tracker', 'PlayerResourceInstance')
    RollLog = apps.get_model('resource_tracker', 'RollLog')

    for game_instance in GameInstance.objects.all():
        for player in game_instance.players.all():
            game_player = GamePlayer.objects.create(
                game_instance=game_instance,
                player=player
            )

            PlayerResourceInstance.objects.filter(
                game_instance=game_instance,
                owner=player
            ).update(
                game_player = game_player
            )

            RollLog.objects.filter(
                game_instance=game_instance,
                player=player
            ).update(
                game_player = game_player
            )


class Migration(migrations.Migration):

    dependencies = [
        (
            "resource_tracker",
            "0006_alter_rolllogentry_die_alter_rolllogentry_face_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(migrate_players)
    ]
