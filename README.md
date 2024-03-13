# Personalized Workout Plan system (PWPs)

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/lasha-chipashvili-github/Sweeft_Acceleration_Task
$ cd Sweeft_Acceleration_Task
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

After database migrations, in order to populate database with predefined exercises run next command in the termina:

```sh
(env)$ python3 manage.py loaddata exercises
```