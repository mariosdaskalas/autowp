from subprocess import call

print("Tested with WordPress Version: 6.6.2")
print('''
              _                      
             | |                     
   __ _ _   _| |_ _____      ___ __  
  / _` | | | | __/ _ \ \ /\ / / '_ \ 
 | (_| | |_| | || (_) \ V  V /| |_) |
  \__,_|\__,_|\__\___/ \_/\_/ | .__/ 
                              | |    
                              |_|    
''')
print("[0] : Posts")
print("[1] : Categories")
print("[2] : Tags")
print("[3] : Pages")
print("[4] : User")
choice = int(input("Choose an option: "))

def mass_post():
    mass_posts = int(input("How many default Posts do you want to create? : "))
    for i in range(0, mass_posts):
        call(["python3", "posts.py"])
    print("Posts created with success! :)")

def mass_cat():
    mass_cats = int(input("How many default Categories do you want to create? : "))
    for i in range(0, mass_cats):
        call(["python3", "categories.py"])
    print("Categories created with success! :)")

def mass_tag():
    mass_tags = int(input("How many default Tags do you want to create? : "))
    for i in range(0, mass_tags):
        call(["python3", "tags.py"])
    print("Tags created with success! :)")

def mass_page():
    mass_pages = int(input("How many default Pages do you want to create? : "))
    for i in range(0, mass_pages):
        call(["python3", "pages.py"])
    print("Pages created with success! :)")

def mass_user():
    mass_users = int(input("How many default Users do you want to create? : "))
    for i in range(0, mass_users):
        call(["python3", "user.py"])
    print("Users created with success! Administrator privileges :)")

if choice == 0:
    mass_post()
elif choice == 1:
    mass_cat()
elif choice == 2:
    mass_tag()
elif choice == 3:
    mass_page()
elif choice == 4:
    mass_user()