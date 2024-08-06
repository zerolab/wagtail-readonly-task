from django.apps import AppConfig


class WorkflowsAppConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    label = "wagtail_readonly_task"
    name = "wagtail_readonly_task"
    verbose_name = "Wagtail Read-only Task"

    def ready(self):
        # note: using a monkey patch until https://github.com/wagtail/wagtail/pull/6025 is fixed
        # Currently scheduled for 6.3 in November
        import wagtail_readonly_task.models.monkey_patches  # noqa
