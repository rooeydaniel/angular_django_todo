"""
This is a helper script, it knows how to handle common management tasks:
    - Start up a development Web server
    - Create new application modules
    - Set up your database

It is recommended that you use django-admin.py
"""
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
