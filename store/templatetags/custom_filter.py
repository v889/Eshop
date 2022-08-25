from django import template
register=template.Library()

@register.filter(name='currency') #name fot templates
def currency(number):
    return "₹ " + str(number)
@register.filter(name='ruppee')
def rupee(number):
    return str(number)
@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

