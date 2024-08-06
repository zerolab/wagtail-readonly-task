from django import template
from wagtail.models import Task

from wagtail_readonly_task.models import ReadOnlyGroupTask


register = template.Library()


@register.filter(name="is_readonly_task")
def is_readonly_task(task: Task | None) -> bool:
    return isinstance(task, ReadOnlyGroupTask)
