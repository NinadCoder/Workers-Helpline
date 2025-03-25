# workers_board/admin.py
from django.contrib import admin
from .models import WorkerDetail

class WorkerDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'worker_type', 'address', 'job_profession', 'wage', 'police_verified']
    search_fields = ['user__username', 'address', 'job_profession']

admin.site.register(WorkerDetail, WorkerDetailAdmin)
