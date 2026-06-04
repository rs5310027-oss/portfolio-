
##E-commerce Customer Behavior Analysis using MySQL##

SELECT * FROM projects.`e-commerce customer behavior analysis`;


#Data Cleaning Functions#
#Check NULL values#

select *
from projects.`e-commerce customer behavior analysis`
where Total_Sales is null;

#Remove duplicates#
DELETE FROM  projects.`e-commerce customer behavior analysis`
WHERE customer_id NOT IN (
SELECT MIN(customer_id)
FROM  projects.`e-commerce customer behavior analysis`
GROUP BY customer_id
);
 
##Remove extra spaces##

SELECT TRIM(product_category)
FROM projects.`e-commerce customer behavior analysis` ;

#Data Exploration Functions#

#Total customers:#

select count(*) as taotal_customers
from projects.`e-commerce customer behavior analysis`;

#Unique product categories:#
SELECT DISTINCT product_category
FROM projects.`e-commerce customer behavior analysis` ;

#Minimum & maximum purchase:#

SELECT MIN(Total_Sales),
MAX(Total_Sales)
FROM projects.`e-commerce customer behavior analysis`;

#Average spending:#

select avg(total_sales)
from projects.`e-commerce customer behavior analysis`;

#Data Transformation Functions#
#Customer spending category# 

SELECT total_sales,
CASE
WHEN Total_Sales  < 500 THEN 'Low'
WHEN Total_Sales BETWEEN 500 AND 2000 THEN 'Medium'
ELSE 'High'
END AS spending_level
FROM  projects.`e-commerce customer behavior analysis`;

#Create total revenue column

SELECT quantity * Total_Sales AS total_revenue
FROM projects.`e-commerce customer behavior analysis`;

# Data Analysis Functions
# Sales by category

SELECT product_category,
SUM(Total_sales)
FROM  projects.`e-commerce customer behavior analysis`
GROUP BY product_category;
 
# Average spending by gender

SELECT Customer_Segment,
AVG(total_sales)
FROM projects.`e-commerce customer behavior analysis`
GROUP BY Customer_Segment;

# Most active customers

SELECT customer_name,
COUNT(*) AS Total_sales
FROM projects.`e-commerce customer behavior analysis`
GROUP BY customer_name
ORDER BY Total_Sales DESC
limit 5;

# Monthly sales trend

SELECT MONTH(order_date) AS month,
SUM(Total_Sales)
FROM projects.`e-commerce customer behavior analysis`
GROUP BY month;

# Advanced SQL Functions
# Rank customers by spending

SELECT customer_name,
Total_sales,
RANK() OVER(ORDER BY Total_sales DESC) AS rank_num
FROM projects.`e-commerce customer behavior analysis`;

# Running total

SELECT order_date,
SUM(Total_sales)
OVER(ORDER BY order_date) AS running_sales
FROM projects.`e-commerce customer behavior analysis`;