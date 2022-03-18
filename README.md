# ProjecteWeb_Practica1
TODO:
//Per poder carregar les vistes heu d'anar a settings.py de BoogeyBook i canviar el path del directori de TEMPLATES pel vostre.
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/victor/Enginyeria Informàtica/3r Curs/Projecte Web/BoogeyBook/BoogeyBook/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Altres comandes necessaries:**

//Per executar el servidor
$python manage.py runserver

//Per entrar a la pàgina web:
url: localhost:8000/home
