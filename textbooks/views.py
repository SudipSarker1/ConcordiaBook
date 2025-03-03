from django.shortcuts import render
from .models import Textbook

def textbook_list(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
    context = {
        'course_code': course_code,
        'textbooks': textbooks,
    }
    return render(request, 'textbooks/textbook_list.html', context)
