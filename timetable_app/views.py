from .models import Trainer, Utilization
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            trainer = self.request.user.trainer
            sessions = Utilization.objects.filter(trainer=trainer)
            today = timezone.now().date()
            events = []
            for util in sessions:
                start_dt = timezone.make_aware(datetime.combine(util.session_date, util.start_time))
                end_dt = timezone.make_aware(datetime.combine(util.session_date, util.end_time))
                events.append({
                    'title': util.course_name,
                    'start': start_dt.isoformat(),
                    'end': end_dt.isoformat(),
                    'extendedProps': {
                        'summary': f"{util.course_name} - {util.start_time.strftime('%H:%M')} to {util.end_time.strftime('%H:%M')} at {util.location or 'N/A'}",
                        'highlight': util.session_date == today,
                        'category': util.category
                    }
                })
            context['events'] = events
        except Trainer.DoesNotExist:
            context['error'] = "You are not registered as a trainer."
        return context

def custom_logout(request):
    logout(request)
    messages.info(request, "You are logged out.")
    return redirect('login')

@login_required
def admin_schedule(request):
    if not request.user.is_superuser:
        return render(request, 'timetable_app/unauthorized.html', {'error': "You must be an admin."})
    utilizations = Utilization.objects.all()
    today = timezone.now().date()
    events = [
        {
            'title': util.course_name,
            'start': timezone.make_aware(datetime.combine(util.session_date, util.start_time)).isoformat(),
            'end': timezone.make_aware(datetime.combine(util.session_date, util.end_time)).isoformat(),
            'extendedProps': {
                'summary': f"{util.course_name} - {util.start_time.strftime('%H:%M')} to {util.end_time.strftime('%H:%M')} at {util.location or 'N/A'} (Trainer: {util.trainer.name})",
                'highlight': util.session_date == today,
                'category': util.category
            }
        }
        for util in utilizations
    ]
    return render(request, 'calendar.html', {'events': events, 'error': None})