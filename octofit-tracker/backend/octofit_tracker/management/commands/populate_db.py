
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Clear existing data
		Activity.objects.all().delete()
		Leaderboard.objects.all().delete()
		User.objects.all().delete()
		Team.objects.all().delete()
		Workout.objects.all().delete()

		# Create Teams
		marvel = Team.objects.create(name='marvel', description='Marvel Team')
		dc = Team.objects.create(name='dc', description='DC Team')

		# Create Users
		users = [
			User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
			User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name),
			User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
			User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
		]

		# Create Activities
		Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
		Activity.objects.create(user=users[1], type='cycle', duration=45, date=timezone.now().date())
		Activity.objects.create(user=users[2], type='swim', duration=60, date=timezone.now().date())
		Activity.objects.create(user=users[3], type='yoga', duration=20, date=timezone.now().date())

		# Create Workouts
		Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy')
		Workout.objects.create(name='Squats', description='Lower body', difficulty='medium')
		Workout.objects.create(name='Plank', description='Core', difficulty='hard')

		# Create Leaderboard
		Leaderboard.objects.create(team=marvel, points=150)
		Leaderboard.objects.create(team=dc, points=120)

		self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
