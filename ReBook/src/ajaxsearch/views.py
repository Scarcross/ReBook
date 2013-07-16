from django.shortcuts import render_to_response


def ajax_example(request):
    if not request.POST:
        return render_to_response('ajax/ajax_example.html', {})
    response_dict = {}
    name = request.POST.get('name', False)
    total = request.POST.get('total', False)
    response_dict.update({'name': name, 'total': total})
    if total:
        try:
            total = int(total)
        except:
            total = False
    if name and total and int(total) == 10:
        response_dict.update({'success': True })
    else:
        response_dict.update({'errors': {}})
        if not name:
            response_dict['errors'].update({'name': 'This field is required'})
        if not total and total is not False:
            response_dict['errors'].update({'total': 'This field is required'})
        elif int(total) != 10:
            response_dict['errors'].update({'total': 'Incorrect total'})
    return render_to_response('weblog/ajax_example.html', response_dict)