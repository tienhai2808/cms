from django import template
from django.utils.timezone import now
from datetime import timedelta

register = template.Library()

@register.filter
def first_sentence(value):
    if value:
        sentences = value.split('.')
        if len(sentences) > 0:
            return sentences[0] + '.'
    return value

@register.filter
def custom_time_display(value):
    time_diff = now() - value
    if time_diff < timedelta(minutes=1):
        return "Vừa xong"
    elif time_diff < timedelta(hours=1):
        minutes = int(time_diff.total_seconds() // 60)
        return f"{minutes} phút trước"
    elif time_diff < timedelta(days=1):
        hours = int(time_diff.total_seconds() // 3600)
        return f"{hours} giờ trước"
    else:
        days = time_diff.days
        return f"{days} ngày trước"