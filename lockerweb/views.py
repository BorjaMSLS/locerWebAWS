import requests
from django.shortcuts import render, redirect
from django.conf import settings

def user_list(request):
    url = f'http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getUsers'
    response = requests.get(url)
    users = response.json()
    return render(request, 'user_list.html', {'users': users})


def authenticate_staff(request):
    if request.method == 'POST':
        # Extract the username and password from the form data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Construct the URL for the Flask endpoint
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/authenticate/{email}/{password}"

        # Send a GET request to the Flask endpoint
        response = requests.get(url)
        print(repr(response.text))
        print(response.text)
        print(response.status_code)

        # Check the response status code to see if the request was successful
        if 'Staff access granted' in response.text:
            # Authentication succeeded
            return redirect('front_desk')
        elif 'User access granted' in response.text:
            # Authentication succeeded
            return redirect('user_profile',email=email)
        else:
            # Authentication failed
            return redirect('login')
    else:
        # Render the login form template
        return render(request, 'login.html')


def main(request):
    return render(request, 'main.html', {'title': 'User list'})

def login(request):
    return render(request, 'login.html', {'title': 'Login page'})

def center_list(request):
    # Make a request to API to retrieve the list of centers
    url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getCenters/"
    response = requests.get(url)
    centers = response.json()

    return render(request, 'front_desk.html', {'centers': centers})

def front_desk(request):
    if request.method == 'POST':
        club = request.POST.get('club')
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getLockers/{club}"
        response = requests.get(url)
        lockers = response.json()
        context = {'lockers': lockers, 'selected_club': club}
        if request.POST.get('refresh'):
            return redirect('front_desk')
        else:
            return render(request, 'front_desk.html', context)
    elif request.method == 'GET':
        club = request.POST.get('club')
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getLockers/6"
        response = requests.get(url)
        lockers = response.json()
        context = {'lockers': lockers, 'selected_club': club}
        if request.GET.get('refresh'):
            return redirect('front_desk')
        else:
            return render(request, 'front_desk.html', context)

def user_profile(request, email):


    url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getPersonLockers/{email}"
    print(url)
    response = requests.get(url)
    lockers = response.json()

    return render(request, 'user_profile.html', {'lockers': lockers})

def locker_menu(request, locker_id):
    url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/getLockerAtt/{locker_id}"
    response = requests.get(url)
    if '"status": "RENTED"' in response.text:
        return redirect('locker_menu_staff_release', locker_id)

    else:
        return redirect('locker_menu_staff_rent', locker_id)

def locker_menu_user(request, locker_id):
    return render(request, 'locker_menu.html')

def locker_menu_staff_release(request, locker_id):
    context = {'selected_locker': locker_id}
    return render(request, 'locker_menu_staff_release.html', context)

def locker_menu_staff_release_confirm(request, locker_id):
    url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/releaseLocker/{locker_id}"
    print(locker_id)
    response = requests.post(url)
    if 'Locker released' in response.text:
        return redirect('success')
    else:
        return redirect('locker_menu_staff_release_confirm')



def locker_menu_staff_rent_confirm(request, locker_id, user_id):
    #render(request, 'locker_menu_staff_rent_confirm.html', {'title': 'Locker Menu'})
    if request.method == 'GET':
        print(locker_id)
        payload = {
            'locker_id': locker_id,
            'user_id': user_id
        }
        response = requests.post(f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/assignLocker", json=payload)
        if 'Locker successfully assigned' in response.text:
            return redirect('success')
    else:
        return redirect('locker_menu_staff_rent_confirm')

def capture_user(request):
    return render(request, 'capture_user.html')


def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        print(email)
        payload = {
            'name': name,
            'email': email
        }
        response = requests.post(f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/newUser", json=payload)
        return redirect('user_list')
    else:
        return 'error'

def assign_locker(request, locker_id, user_name):
    if request.method == 'GET':
        print(locker_id)
        payload = {
            'name': user_name,
            'lokcer_id': locker_id
        }
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/findByEmail/{search}"
        response = requests.get(url)
        users = response.json()
        return render(request, 'locker_menu_staff_rent.html', {'users': users})




def search_user(request, locker_id):
    if request.method == 'POST':
        print(locker_id)
        search = request.POST.get('search')
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/findByEmail/{search}"
        response = requests.get(url)
        users = response.json()
        context = {'users': users, 'selected_locker': locker_id}
        return render(request, 'locker_menu_staff_rent.html', context)
    elif request.method == 'GET':
        search = request.POST.get('search')
        print(locker_id)
        url = f"http://{settings.SERVER_API_IP}:{settings.SERVER_API_PORT}/findByEmail/ "
        response = requests.get(url)
        users = response.json()
        context = {'users': users, 'selected_locker': locker_id}
        return render(request, 'locker_menu_staff_rent.html', context)

def success(request):
    return render(request, 'success.html')







