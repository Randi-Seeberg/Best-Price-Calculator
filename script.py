def cost_ground_shipping(weight):
  if weight<=2:
    return weight*1.50+20
  if 2<weight<=6:
    return weight*3.00+20
  if 6<weight<=10:
    return weight*4.00+20
  if weight>10:
    return weight*4.75+20
  cost=cost_ground_shipping(weight)
  return cost
#print(cost_ground_shipping(8.4))
#Udskriver prisen for ground shipping.
cost_premium_shipping=125.00
def cost_drone_shipping(weight):
  if weight<=2:
    return weight*4.50
  if 2<weight<=6:
    return weight*9.00
  if 6<weight<=10:
    return weight*12.00
  if weight>10:
    return weight*14.25
#print(cost_drone_shipping(1.5))
def cheapest_shipping(weight):
  if cost_ground_shipping(weight) < cost_premium_shipping and cost_ground_shipping(weight) < cost_drone_shipping(weight):
    print("The cheapest shipping method for your parcel is ground shipping. The cost will be "+str(cost_ground_shipping(weight))+" USD.")
  if cost_premium_shipping < cost_ground_shipping(weight) and cost_premium_shipping < cost_drone_shipping(weight):
    print("The cheapest shipping method for your parcel is premium shipping. The cost will be "+str(cost_premium_shipping)+" USD.")
  if cost_drone_shipping(weight) < cost_ground_shipping(weight) and cost_drone_shipping(weight) < cost_premium_shipping:
    print("The cheapest shipping method for your parcel is drone shipping. The cost will be "+str(cost_drone_shipping(weight))+" USD.")
cheapest_shipping(41.5)

   