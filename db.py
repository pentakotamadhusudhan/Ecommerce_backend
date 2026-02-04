


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce_db',  # The name of your MySQL database
        'USER': 'root',      # Your MySQL username (e.g., 'root')
        'PASSWORD': 'Madhu@12',  # Your MySQL password
        'HOST': '127.0.0.1',          # Or the IP address of your MySQL server
        'PORT': '3306',               # The default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # Recommended for data integrity
        }
    }
}
