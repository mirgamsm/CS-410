from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Tutor(models.Model):
    PHONICS_CHOICES = (
        ('Fundations', 'Fundations'),
        ('Fountas & Pinnell Literacy', 'Fountas & Pinnell Literacy'),
        ('Lucy Calkins Units Of Study For Teaching Phonics',
         'Lucy Calkins Units Of Study For Teaching Phonics'),
        ('Bridge The Gap Intervention', 'Bridge The Gap Intervention'),
        ('Words Their Way', 'Words Their Way'),
        ('Lalilo', 'Lalilo'),
        ('The Heggerty Curriculum', 'The Heggerty Curriculum'),
        ('Orton Gillingham Approach', 'Orton Gillingham Approach'),
        ('Phonics First', 'Phonics First'),
        ('Other', 'Other')
    )
    EMPLOYMENT_CHOICES = (
        ('Fulltime', 'Fulltime'),
        ('Part Time', 'Part Time'),
        ('College Student', 'College Student'),
        ('Retired', 'Retired'),
        ('Other', 'Other')

    )
    STATE_CHOICES = (
        (
            ('AL','AL'),
            ('AK','AK'),
            ('AR','AR'),
            ('AZ','AZ'),
            ('CA','CA'),
            ('CO','CO'),
            ('CT','CT'),
            ('DC','DC'),
            ('DE','DE'),
            ('FL','FL'),
            ('GA','GA'),
            ('HI','HI'),
            ('IA','IA'),
            ('ID','ID'),
            ('IL','IL'),
            ('IN','IN'),
            ('KS','KS'),
            ('KY','KY'),
            ('LA','LA'),
            ('MA','MA'),
            ('MD','MD'),
            ('ME','ME'),
            ('MI','MI'),
            ('MN','MN'),
            ('MO','MO'),
            ('MS','MS'),
            ('MT','MT'),
            ('NC','NC'),
            ('NE','NE'),
            ('NH','NH'),
            ('NJ','NJ'),
            ('NM','NM'),
            ('NV','NV'),
            ('NY','NY'),
            ('ND','ND'),
            ('OH','OH'),
            ('OK','OK'),
            ('OR','OR'),
            ('PA','PA'),
            ('RI','RI'),
            ('SC','SC'),
            ('SD','SD'),
            ('TN','TN'),
            ('TX','TX'),
            ('UT','UT'),
            ('VT','VT'),
            ('VA','VA'),
            ('WA','WA'),
            ('WI','WI'),
            ('WV','WV'),
            ('WY','WY'),
            ('None','None')
        )
    )
    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('Chinese', 'Chinese'),
        ('Other', 'Other'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-Binary', 'Non-Binary'),

    )
    DEGREE_CHOICES = (
        ('None', 'None'),
        ('CIN', 'Currently Enrolled In College'),
        ('AS', 'Associate'),
        ('TECH', 'Technical Certification'),
        ('BAS', 'BA/BS/Etc . . .'),
        ('MA', 'MA/MS/Etc...'),
        ('ED', 'Education Specialist/6th Year/Etc . . .'),
        ('EDD', 'ED.D/PH.D/Etc . . .')
    )
    YESNO = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    AVAILABILITY_CHOICES = (
        ('AM', 'Part Time AM'),
        ('PM', 'Full Time PM')
    )
    firstname = models.CharField(max_length=20, blank=True)
    lastname = models.CharField(max_length=20, blank=True)
    phonenumber = models.CharField(max_length=12, blank=True, verbose_name='Phone Number')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    introduction = models.TextField(blank=True, verbose_name='Introduction (200 Words or less)')
    languages = MultiSelectField(choices=LANGUAGE_CHOICES, default="English")
    education = models.CharField(max_length=60, choices=DEGREE_CHOICES, blank=True, default='HS')
    major = models.CharField(max_length=20, blank=True, verbose_name='Major (If Applicable)')
    minor = models.CharField(max_length=20, blank=True, verbose_name='Minor (If Applicable)')
    experience = models.CharField(max_length=4, choices=YESNO, blank=True, verbose_name='Are You A Certified Teacher?')
    statecert = models.CharField(max_length=5, choices=STATE_CHOICES, verbose_name='Please Choose The State You Are Certified In:', default='None')
    phonicsex = MultiSelectField(choices=PHONICS_CHOICES, blank=True, verbose_name='Choose Any Phonics Programs You Have Experience With:')
    employment = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, blank=True)
    curremployment = models.CharField(max_length=30, blank=True)
    employer = models.CharField(max_length=20, blank=True, verbose_name='Employer')
    employeraddress = models.CharField(max_length=30, blank=True, verbose_name='Employer Address')
    currreference = models.CharField(max_length=20, blank=True, verbose_name='Supervisor/Reference Contact Information:')
    teachercharacteristics = models.TextField(max_length=200, blank=True, verbose_name='What Characteristics Make A Good Teacher: (200 Words or less)')
    abilitiesquestion = models.TextField(max_length=200, blank=True, verbose_name='How Would You Address A Range Of Abilities In Your Classroom: (200 Words or less)')
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, blank=True, verbose_name='Choose Your Availability:')
    owner = models.CharField(max_length=150, blank=True)
