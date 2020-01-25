from wagtail.core.models import Page


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context['services'] = ['Financial Advisory', 'Strategy and Operations', 'Valuations']
        return context
    pass
