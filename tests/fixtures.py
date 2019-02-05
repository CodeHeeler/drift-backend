AUTH_HEADER = {'X-RH-IDENTITY': 'eyJpZGVudGl0eSI6eyJhY2NvdW50X251bWJlciI6Ij'
                                'EyMzQiLCJ0eXBlIjoiVXNlciIsInVzZXIiOnsidXNl'
                                'cm5hbWUiOiJ0ZXN0X3VzZXJuYW1lIiwiZW1haWwiOi'
                                'J0ZXN0QGV4YW1wbGUuY29tIiwiZmlyc3RfbmFtZSI6'
                                'IkZpcnN0bmFtZSIsImxhc3RfbmFtZSI6Ikxhc3RuYW'
                                '1lIiwiaXNfYWN0aXZlIjp0cnVlLCJpc19vcmdfYWRt'
                                'aW4iOmZhbHNlLCJpc19pbnRlcm5hbCI6dHJ1ZSwibG'
                                '9jYWxlIjoiZW5fVVMifSwiaW50ZXJuYWwiOnsib3Jn'
                                'X2lkIjoiNTY3OCJ9fX0KCg=='}

FETCH_HOSTS_RESULT = [
    {
      "account": "9876543",
      "bios_uuid": "e380fd4a-28ae-11e9-974c-c85b761454fa",
      "created": "2019-01-31T13:00:00.100010Z",
      "display_name": None,
      "facts": [],
      "fqdn": "fake_host_99.example.com",
      "id": "fc1e497a-28ae-11e9-afd9-c85b761454fa",
      "insights_id": "01791a58-28af-11e9-9ab0-c85b761454fa",
      "ip_addresses": [
        "10.0.0.3",
        "2620:52:0:2598:5054:ff:fecd:ae15"
      ],
      "mac_addresses": [
        "52:54:00:cd:ae:00",
        "00:00:00:00:00:00"
      ],
      "rhel_machine_id": None,
      "satellite_id": None,
      "subscription_manager_id": "RHN Classic and Red Hat Subscription Management",
      "tags": [],
      "updated": "2019-01-31T14:00:00.500000Z"
    }]

HOST_TEMPLATE = '''
    {
      "count": 1,
      "page": 1,
      "per_page": 50,
      "results": [
    {
      "account": "1234567",
      "bios_uuid": "dc43976c263411e9bcf0c85b761454fa",
      "created": "2018-12-01T12:00:00.000000Z",
      "display_name": "host1.example.com",
      "facts": [
        {
          "facts": {},
          "namespace": "string"
        }
      ],
      "fqdn": "host.example.com",
      "id": "%s",
      "insights_id": "TEST-ID00-0000-0000",
      "ip_addresses": [
        "10.0.0.1",
        "10.0.0.2"
      ],
      "mac_addresses": [
        "c2:00:d0:c8:00:01"
      ],
      "subscription_manager_id": "1234FAKE1234",
      "tags": [],
      "updated": "2018-12-31T12:00:00.000000Z"
    }]}'''