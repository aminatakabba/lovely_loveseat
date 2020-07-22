def ground_shiping(weight):
  base_price = 20.0
  if weight <= 2:
    return 1.25*weight + base_price
  elif weight <= 6:
    return 3*weight + base_price
  elif weight <= 10:
    return 4*weight + base_price
  else:
    return 4.75*weight + base_price

print(ground_shiping(8.4))

premium_shiping = 125.0

def drone_shiping(weight):
  if weight <= 2:
    return 4.5*weight
  elif weight <= 6:
    return 9*weight
  elif weight <= 10:
    return 12*weight
  else:
    return 14.25*weight

print(drone_shiping(1.5))

def best_price(weight):
  ground = ground_shiping(weight)
  drone = drone_shiping(weight)
  premium = premium_shiping

  if ground > drone and drone > premium:
    method = "premium ground"
    cost = premium
  elif drone > ground and premium > ground:
    method = "standard ground"
    cost = ground
  else:
    method: "drone"
    cost = drone
  print(
    "The cheapest method is $%.2f with %s shiping."
    %(cost, method)
  )

best_price(4.6)