# sexshop_parser
# Python 3.6.7

# Run parser on hosting server
# after git pull, as root user change permissions on sexshop_parser to user www-data using this command:
# chown www-data: sexshop_parser/

# Cron command in crontab for running every 48h
# * */48 * * * su -p www-data -c "/var/www/sexshop_parser/.venv/bin/python /var/www/sexshop_parser/manage.py 
# erosklad_scraper"
