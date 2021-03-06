
# CRUD application(blog website) using Flask and MySQL.

This is a blog website. It is basically a backend intended project that I worked on to get my hands dirty with backend technologies.

I have used a microframework named flask in my project.



## Demo

https://my-code-blogg.herokuapp.com/


## Features

- Admin login/logout
- All the CRUD operations can be done by the admin.
- Anyone can contact using contact form


  
## Tech used

**Language:** Python

**Frontend:** Bootstrap

**Backend Framework:** Flask

**Database:** SQL database



## Run Locally

Make an empty directory, open terminal in it and run the following commands.

Clone the project

```bash
  git clone https://github.com/anipnwr7777/my_blog.git
```

Install all the dependencies

```bash
  pip install -r requirements.txt
```

Open Xampp as localhost and make a new database named codethunder with two tables named contacts ans posts. Replicate them as shown in the screenshots.

contacts:
![image](https://user-images.githubusercontent.com/42828778/125503952-bca3f52a-ca35-46b1-9a87-4ce9d705c268.png)

posts:
![image](https://user-images.githubusercontent.com/42828778/125504048-3ec62472-d4ff-43e2-874e-9d07e81c8c2c.png)


Open config.json and modify: // "local_uri" : "mysql+pymysql://root:@localhost/codethunder"

Run the file main.py

```bash
  python main.py
```

Go to your browser and type http://127.0.0.1:5000/ in the address bar.

Hurray!! you are all set.
  
## Deployment

This project is deployed on Heroku server with the database on freesqldatabase.

  
## Contributing

Contributions are always welcome!


  
