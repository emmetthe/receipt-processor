import math
from datetime import datetime

def calculate_points(receipt):
  points = 0
  retailer = receipt['retailer']
  total = receipt['total']
  items = receipt['items']
  purchase_date = receipt['purchaseDate']
  purchase_time = receipt['purchaseTime']

  # One point for every alphanumeric character in the retailer name
  count = 0
  for char in retailer:
    if char.isalnum():
      count += 1
  points += count

  # 50 points if the total is a round dollar amount with no cents
  if float(total) == int(float(total)):
    points += 50

  # 25 points if the total is a multiple of 0.25
  if float(total) % 0.25 == 0:
    points += 25

  # 5 points for every two items on the receipt
  points += (len(items) // 2) * 5

  # Points for item description length and price
  for item in items:
    desc = item['shortDescription'].strip()
    price = item['price']
    if len(desc) % 3 == 0:
      points += math.ceil(float(price) * 0.2)

  # 6 points if the day in the purchase date is odd
  if datetime.strptime(purchase_date, "%Y-%m-%d").day % 2 != 0:
    points += 6

  # 10 points if the time of purchase is after 2:00pm and before 4:00pm
  time = datetime.strptime(purchase_time, "%H:%M")
  if 14 <= time.hour < 16:
    points += 10

  return points
