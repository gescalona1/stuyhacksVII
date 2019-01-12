from django.db import models
import datetime
# Create your managers here


class AppointmentManager(models.Manager):
    use_in_migrations = True

    def create_appointment(self, title, description, address, geolocation, due_time, member):
        if not title:
            raise ValueError('The title is not valid')
        appointment = self.model(title=title,
                           description=description,
                           address=address,
                           geolocation=geolocation,
                           due_time=due_time,
                           member=member
        )
        appointment.save(using=self._db)
        return appointment
