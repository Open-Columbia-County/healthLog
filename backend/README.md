# Backend - Django REST API

## Base URL
- Deployed - TBD
- http://localhost:8000/
- http://127.0.0.1:8000/

## Admin
- py manage.py createsuperuser
- py manage.py runserver
- BaseURL/admin/

## API
- api/

### Auth
- api/auth/login
    - email
    - password
- api/auth/register
    - email
    - username
    - password
- api/auth/refresh

### User
- user/
    - Authentication needed
    - In postman login on one tab auth is provided for others
    - All Fields
        - username
        - email
        - is_active
        - is_staff (can be used for provider access?)
        - diabetic (show hide sugar pages)
        - password


### Data
- symptom/
    - Admin only add/edit/update/delete
    - symptom
    - info
- medication/
    - Not user specific
    - name
    - freq (frequency taken daily, 3x a day)
- week/
    - title
    - writer (user.id)
- log/
    - day
    - title
    - content
    - week (week.id)
    - author (user.id)
- mood/
    - tag
    - date
    - mood
    - symptom (symptom.id)
    - log (log.id)
    - user (user.id)
- taken/
    - when
    - dose
    - medication (medication.id)
    - day (log.id)
    - member (user.id)
- sugar/
    - time
    - level
    - note (log.id)
    - owner (user.id)
- provider/ (Patient Table)
    - patient (logged in user.id)
    - provider (different user.id)
- food/
    - food
    - calories
    - date
    - theDay (log.id)
    - person (user.id)