
USE CustomerChurnDB;
GO

-- 1. Check total number of customers
SELECT COUNT(*) AS TotalCustomers
FROM dbo.customer_churn;
GO

-- 2. Check overall churn count
SELECT Churn, COUNT(*) AS CustomerCount
FROM dbo.customer_churn
GROUP BY Churn;
GO

-- 3. Churn by contract type
SELECT
    Contract,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    CAST(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercent
FROM dbo.customer_churn
GROUP BY Contract
ORDER BY ChurnRatePercent DESC;
GO

-- 4. Churn by payment method
SELECT
    PaymentMethod,
    COUNT(*) AS TotalCustomers,
    CAST(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercent
FROM dbo.customer_churn
GROUP BY PaymentMethod
ORDER BY ChurnRatePercent DESC;
GO

-- 5. Average tenure by churn status
SELECT
    Churn,
    AVG(TRY_CAST(tenure AS FLOAT)) AS AverageTenureMonths
FROM dbo.customer_churn
GROUP BY Churn;
GO

-- 6. Average monthly charges by churn status
SELECT
    Churn,
    AVG(TRY_CAST(MonthlyCharges AS FLOAT)) AS AverageMonthlyCharges
FROM dbo.customer_churn
GROUP BY Churn;
GO