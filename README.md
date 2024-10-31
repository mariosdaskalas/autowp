This is a Python program that automates various tasks in the
WordPress CMS.

Posts : wp_title_{i} / Lorem Ipsum

Categories : wp_cat_{i}

Tags : wp_tag_{i}

Pages : wp_title_{i} / Lorem Ipsum

Users :

random_username

first_{random_username}

last_{random_username})

random_nickname

random_email@wp.local

https://example.com/

password : password

To execute the program first run the following commands.
```
pip3 install playwright
playwright install
```

To automate a process using the browser run
```
playwright codegen
```

Inside the data folder, in the target.txt place the domain
that the WordPress host is.
In the credentials.txt place the username and password
in the format of root:root respectively.

Run the program with:
```
python3 autowp.py
```

Tested with WordPress Version: 6.6.2