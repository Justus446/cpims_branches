from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

from cpovc_settings.forms import SettingsForm


@login_required
def ovc_dashboard(request):
    """Method to do pivot reports."""
    try:
        form = moble()
        return render(
            request, 'dashboards/ovc_dashboard.html',
            {'form': form, 'colors': dcolors})
    except Exception as e:
        raise e
    else:
        pass