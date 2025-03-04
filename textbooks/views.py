# textbooks/views.py

from django.shortcuts import render
from .models import Textbook

def textbook_list(request):
    """
    Shows all available textbooks by default.
    If 'course_code' is provided in GET, filters by that code.
    Displays a 'no textbooks' message if none are found.
    """
    # Start with all available textbooks
    textbooks = Textbook.objects.filter(availability=True)

    # For the left-side filter: distinct course codes
    course_codes = Textbook.objects.values_list('course_code', flat=True).distinct()

    # Check if the user submitted a course code in the query parameters
    code = request.GET.get('course_code', '').strip()
    if code:
        textbooks = textbooks.filter(course_code=code)

    context = {
        'textbooks': textbooks,
        'course_codes': course_codes,
        'selected_code': code,  # to remember what the user typed
    }
    return render(request, 'textbooks/textbook_list.html', context)
