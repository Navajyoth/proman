import datetime
from fabric.api import *
from fabric.contrib import django
from fabric.operations import run, put
from fabric.api import run, env, run, cd, prefix, local
from fabric.colors import *

env.user = "root"
env.hosts = ['128.199.129.205']
remote_dir = '/home'
project_name = 'proman'
code_dir = remote_dir + '/' + project_name
backup_dir = '/home/backups/proman'
target_dir = '~'


def deploy():
       with cd(code_dir):
         run("source /home/proman/bin/activate && pip list")
         install_requirements()
         run("git pull")
         migrate()
         run_test()
         collectstatic()
         restart_app()


def install_requirements():
    with cd(code_dir):
       run("source /home/proman/bin/activate && pip install -r requirements.txt")

def migrate():
    with cd(code_dir):
       run("source /home/proman/bin/activate && python manage.py migrate --noinput")

def run_test():
    with cd(code_dir):
        print yellow("Test is going to start")
        run("source /home/proman/bin/activate && python manage.py test")


def collectstatic():
    with cd(code_dir):
         run("source /home/proman/bin/activate && python manage.py collectstatic --noinput")

def backup():
     with cd(remote_dir):
        sudo("source proman_backup.sh")

def copy_dump():
    get('/home/backups/proman', target_dir)

def restart_app():
    print red("Restarting gunicorn.............")
    sudo("supervisorctl restart all")
