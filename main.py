import requests

# Register new webhook for earnings
r = requests.post('https://finnhub.io/api/v1/webhook/add?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg', json={'event': 'earnings', 'symbol': 'AAPL'})
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get('https://finnhub.io/api/v1/webhook/list?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg')
res = r.json()
print(res)

#Delete webhook
r = requests.post('https://finnhub.io/api/v1/webhook/delete?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg', json={'id': webhook_id})
res = r.json()
print(res)
