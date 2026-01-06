import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()

# Auto-migrate on startup (Hack for Render without shell access)
try:
    call_command('migrate')
except Exception as e:
    print(f"Auto-migration failed: {e}")
