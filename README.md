# Media Hosting

This Sample Django project allows multiple file upload (Image/Video) into seperate folder depending on file type.

List media dir in a hierarchy.

-->year

---->month

------>day

-------->video/pictures

---------->file

Dependency

#1 jQuery fileupload plugin

#2 Django filebrowser (for browsable media dir listing)


![alt home](https://preview.ibb.co/gFosfd/home.png)

![alt home](https://preview.ibb.co/hAauty/folder.png)


## Running Locally

```bash
git clone https://github.com/basiljose1/mediahost.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```
