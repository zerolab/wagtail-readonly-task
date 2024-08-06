import wagtail.admin.views.pages.edit

from wagtail_readonly_task.models.views import EditView as OverriddenView


wagtail.admin.views.pages.edit.EditView.as_view = OverriddenView.as_view
