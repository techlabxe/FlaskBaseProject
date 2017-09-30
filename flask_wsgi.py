from project import create_app
import sys,os

# 配置される場所に変更すること.
sys.path.append('/var/www/flask/myproject')

application = create_app('production')
