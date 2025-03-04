# textbooks/views.py

from django.shortcuts import render, redirect
from .models import Textbook

def textbook_list(request, course_code=None):
    """
    Displays all textbooks by default (at /textbooks/).
    If 'course_code' is in the GET data, redirect to /textbooks/<that code>.
    If the URL includes /textbooks/<course_code>/, show only that course.
    Uses ONE template: textbook_list.html
    """
    # 1) If the user typed a code in the filter form (?course_code=XYZ),
    #    redirect to /textbooks/XYZ/
    typed_code = request.GET.get('course_code', '').strip()
    if typed_code:
        return redirect('textbook_list_with_code', course_code=typed_code)

    # 2) If we have a course_code in the URL, filter by that
    if course_code:
        textbooks = Textbook.objects.filter(course_code=course_code, availability=True)
        selected_code = course_code
    else:
        # No code in the URL -> show ALL textbooks
        textbooks = Textbook.objects.filter(availability=True)
        selected_code = ''

    # 3) We also want a list of distinct course codes for the left-side filter
    course_codes = Textbook.objects.values_list('course_code', flat=True).distinct()

    context = {
        'textbooks': textbooks,
        'course_codes': course_codes,
        'selected_code': selected_code,  # so we can display it in the form if needed
    }
    return render(request, 'textbooks/textbook_list.html', context)
