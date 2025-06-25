from django.core.management.base import BaseCommand
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from octofit_app.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Populate users
        User.objects.create(email='john.doe@example.com', name='John Doe', age=30)
        User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=25)

        # Populate teams
        team = Team.objects.create(name='Team Alpha')
        team.members.add(User.objects.get(email='john.doe@example.com'))
        team.members.add(User.objects.get(email='jane.smith@example.com'))

        # Populate activities
        Activity.objects.create(user=User.objects.get(email='john.doe@example.com'), type='Running', duration=60, date='2025-06-24')
        Activity.objects.create(user=User.objects.get(email='jane.smith@example.com'), type='Cycling', duration=45, date='2025-06-23')

        # Populate leaderboard
        Leaderboard.objects.create(user=User.objects.get(email='john.doe@example.com'), score=100)
        Leaderboard.objects.create(user=User.objects.get(email='jane.smith@example.com'), score=90)

        # Populate workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run to start the day.', duration=30)
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session.', duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
