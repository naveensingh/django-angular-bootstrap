from django.views.generic.base import TemplateView


class BaseLandingView(TemplateView):
    template_name = "landing/index.html"

    def dispatch(self, *args, **kwargs):
        return super(BaseLandingView, self).dispatch(*args, **kwargs)

        # def get_context_data(self, **kwargs):
        #     context = super(DefaultLandingView, self).get_context_data(**kwargs)
        #     return context
