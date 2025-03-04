from django.shortcuts import render
from .models import Textbook

def textbook_list(request, course_code):
    # Retrieve textbooks for the given course code where they are available
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
    context = {
        'textbooks': textbooks,
        'course_code': course_code,
    }
    return render(request, 'textbooks/textbook_list.html', context)
