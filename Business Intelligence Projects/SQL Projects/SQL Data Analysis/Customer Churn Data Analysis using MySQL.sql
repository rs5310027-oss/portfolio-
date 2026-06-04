## import Data Load CSV into MySQL ##

SELECT * FROM projects.`customer churn analysis`;

## Data Cleaning Functions ##
SELECT *
FROM projects.`customer churn analysis` 
WHERE tenure IS NULL;

UPDATE projects.`customer churn analysis`
SET tenure = 0
WHERE tenure IS NULL;

DELETE FROM projects.`customer churn analysis`
WHERE customerID NOT IN (
SELECT MIN(customerID)
FROM projects.`customer churn analysis`
GROUP BY customerID
);

SELECT TRIM(gender)
FROM projects.`customer churn analysis`;

SELECT DISTINCT Contract
FROM projects.`customer churn analysis` ;


SELECT AVG(MonthlyCharges)
FROM projects.`customer churn analysis` ;

## Data Transformation Functions ##

SELECT tenure,
CASE
WHEN tenure < 12 THEN 'New'
WHEN tenure BETWEEN 12 AND 36 THEN 'Regular'
ELSE 'Loyal'
END AS customer_type
FROM projects.`customer churn analysis` ;

SELECT MonthlyCharges,
CASE
WHEN MonthlyCharges < 50 THEN 'Low'
WHEN MonthlyCharges BETWEEN 50 AND 100 THEN 'Medium'
ELSE 'High'
END AS charge_category
FROM projects.`customer churn analysis`  ;


##Data Analysis Functions##
 
SELECT gender, COUNT(*) AS churn_count
FROM projects.`customer churn analysis`
WHERE Churn='Yes'
GROUP BY gender;

SELECT Contract, COUNT(*) AS churned
FROM projects.`customer churn analysis`
WHERE Churn='Yes'
GROUP BY Contract;


SELECT PaymentMethod, COUNT(*)
FROM projects.`customer churn analysis`
WHERE Churn='Yes'
GROUP BY PaymentMethod;

##Advanced SQL Functions##

SELECT customerID, MonthlyCharges,
RANK() OVER(ORDER BY MonthlyCharges DESC) AS rank_num
FROM projects.`customer churn analysis` ;

SELECT MonthlyCharges,
SUM(MonthlyCharges) OVER(ORDER BY customerID) AS running_total
FROM  projects.`customer churn analysis`;