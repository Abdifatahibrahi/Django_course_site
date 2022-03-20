from django.shortcuts import render


def index(request):
    meetups = [
        {
            'title': ' title of the first meetup',
            'description': 'This is the first meetup',
            'slug': 'a-first-meetup',
        },
        {
            'title': ' title of the second meetup',
            'description': 'This is the second meetup',
            'slug': 'a-second-meetup',
        }
    ]
    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title':'A first meetup',
        'description':'This is the first meetup'
    }
    return render(request, 'meetups/meetups-detail.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })
