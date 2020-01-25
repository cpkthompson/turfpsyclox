from wagtail.core.models import Page


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context['services'] = ['Financial Advisory', 'Strategy and Operations', 'Valuations']
        return context


class ServicesPage(Page):
    pass


class InsightPage(Page):
    pass


class InsightIndexPage(Page):
    pass


class AboutPage(Page):
    pass


class ContactPage(Page):
    pass

