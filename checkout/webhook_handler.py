from django.http import HttpResponse


class StripeWH_Handler:
    # handle stripe webhooks

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handle a generic/unknown/unexpected webhook

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        # handle a payment success webhook

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        # handle a payment failed webhook

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
