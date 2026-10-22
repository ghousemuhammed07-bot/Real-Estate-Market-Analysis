use realestatedb;
select * from properties limit 10;

SELECT COUNT(DISTINCT City) AS Total_Cities
FROM properties;

select Round(Avg(Price),2) as avg_Price
from properties;

select max(Price) as Highest_Price
from properties;

select min(Price) as lowest_Price
from properties;

select City,
Count(*) as Property_count
from properties
group by City;

select property_Name,
City,
Price,
Rank() over(order by Property_Name DESC) as Price_Rank 
from properties
Limit 15;

select Property_Name,
City,
Price,
Row_Number() over(order by Price DESC) as Row_Num
from properties;

WITH CityAvg AS
(
    SELECT City,
           AVG(Price) AS AvgPrice
    FROM properties
    GROUP BY City
)

SELECT p.Property_Name,
       p.City,
       p.Price,
       c.AvgPrice
FROM properties p
JOIN CityAvg c
ON p.City = c.City;


# KPIs

select count(*) as total_Properties
from properties;

select Round(avg(Price),2) as Avg_Price
from properties;

select Round(avg(Area_sqft),2) as Avg_Area
from properties;

select Round(avg(Bedrooms),2) as Avg_Bedrooms
from properties;