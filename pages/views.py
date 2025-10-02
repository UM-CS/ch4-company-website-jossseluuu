from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thanks!",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "12345 University of Montana"
        context["phone_number"] = "(000)000-0000"
        return context

class ProductPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {"name": "MacBook Air", "price": "$999"},
            {"name": "Iphone 17", "price": "$799"},
            {"name": "Ipad", "price": "$349"},
            {"name": "Apple Watch", "price": "$399"}
        ]
        return context