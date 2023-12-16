# LittleLemon
 
Download the entire project

Activate the virtual environment using py-venv/Scripts/activate.bat

All the required libraries are installed in this py-venv environment.


SQL login details
-> mysql -u root -p
->(Enter)

Django superuser details
Username : LittleLemon
password : Lemon@123!

API
(Working and tested)
1)http://127.0.0.1:8000/restaurant/ (static url)
2)http://127.0.0.1:8000/restaurant/menu/items (menu-items -no authentication needed)
3)http://127.0.0.1:8000/restaurant/menu/items/<int:pk> 
4)http://127.0.0.1:8000/restaurant/booking/tables/ (Authentication required)
5)unittesting python - python manage.py test
6)http://127.0.0.1:8000/auth/token/login (Session login using djoser)
7)http://127.0.0.1:8000/auth/token/logout (Seesion logout using djoser)
8)http://127.0.0.1:8000/restaurant/api-token-auth/ (token authentication using DRF)(Create a user in admin and pass those in forms in insomnia in post request)