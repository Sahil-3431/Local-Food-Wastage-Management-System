queries = {

"1.Count Providers by City":
"""
SELECT city,
COUNT(*)
FROM providers
GROUP BY city
""",

"2.Count Receivers by City":
"""
SELECT city,
COUNT(*)
FROM receivers
GROUP BY city
""",

"3.Total Food Quantity by Provider Type":
"""
SELECT provider_type,
SUM(quantity)
FROM food_listings
GROUP BY provider_type
""",

"4.Provider Type Contribution":
"""
SELECT
provider_type,
SUM(quantity) AS total_food
FROM food_listings
GROUP BY provider_type
ORDER BY total_food DESC;
""",

"5.Top Receivers":
"""
SELECT
r.name,
COUNT(*) AS total_claims
FROM claims c
JOIN receivers r
ON c.receiver_id=r.receiver_id
GROUP BY r.name
ORDER BY total_claims DESC;
""",

"6.Total Food Available":
"""SELECT
SUM(quantity) AS total_food_available
FROM food_listings;""",

"7.City with Highest Listings":
"""SELECT
location,
COUNT(*) AS listings
FROM food_listings
GROUP BY location
ORDER BY listings DESC;""",

"8.Most Available Food Type":
"""SELECT
food_type,
COUNT(*) AS total
FROM food_listings
GROUP BY food_type
ORDER BY total DESC;""",

"9.Most Successful Provider":
"""SELECT
p.name,
COUNT(*) AS completed_claims
FROM claims c
JOIN food_listings f
ON c.food_id=f.food_id
JOIN providers p
ON p.provider_id=f.provider_id
WHERE c.status='Completed'
GROUP BY p.name
ORDER BY completed_claims DESC;""",

"10.Claim Status Percentage":

"""SELECT
status,
ROUND(
COUNT(*)*100.0/
(SELECT COUNT(*) FROM claims),
2
) AS percentage
FROM claims
GROUP BY status;""",

"11.Food Expiring Soon":

"""SELECT
food_name,
expiry_date,
quantity
FROM food_listings
WHERE expiry_date <= CURRENT_DATE + INTERVAL '3 days'
ORDER BY expiry_date;""",

"12.Receivers Table":
"""SELECT * FROM receivers;""",

"13.Providers Table":
"""SELECT * FROM providers;""",

"14.Food Listings Table":
"""SELECT * FROM food_listings;"""

}