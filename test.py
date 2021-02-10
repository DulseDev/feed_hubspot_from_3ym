from hubspot import HubSpot
from hubspot.crm.objects import ApiException

hubspot = HubSpot()
# or with api_key
hubspot = HubSpot(api_key='ec94cc63-8761-4d15-a74d-1dc6303f7006')

try:
    deals = hubspot.crm.objects.basic_api.get_page(object_type="deals")
    print(deals)
except ApiException as e:
    print("Exception when requesting custom objects: %s\n" % e)
