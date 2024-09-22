SELECT *
FROM passengers;

-- Gender survived rate
SELECT COUNT(*) AS total_survivors
FROM passengers
WHERE survived = 1;

SELECT sex, 
       COUNT(*) AS total_passengers, 
       SUM(survived) AS survivors,
       (SUM(survived) * 1.0 / COUNT(*)) AS survival_rate
FROM passengers
GROUP BY sex;

-- Group age survived rate

SELECT 
	CASE
		WHEN age <= 12 THEN 'Children'
		WHEN age >= 65 THEN 'Elderly'
		ELSE 'Adults'
END AS age_group,
COUNT (*) AS Total_Passengers,
SUM(survived) AS Survivors,
(SUM(survived) * 1.0 / COUNT (*)) AS Survival_Rate
FROM passengers
WHERE age IS NOT NULL
GROUP BY age_group
ORDER BY Survival_Rate DESC; 


-- Pclass survived rate
SELECT Pclass,
COUNT(*) AS Total_Passengers,
SUM(survived) AS Survivors,
(SUM(survived) * 1.0 / COUNT (*)) AS Survival_Rate
FROM Passengers
GROUP BY Pclass
ORDER BY Pclass;

SELECT AVG(survived) AS Overall_Survival_Rate
FROM Passengers;

SELECT survived,
AVG(age) as Average_Age
FROM passengers
GROUP BY survived;

-- Embarked survived rate		
SELECT embarked, 
       COUNT(*) AS embarked_destination, 
       SUM(survived) AS survivors,
       (SUM(survived) * 1.0 / COUNT(*)) AS survival_rate
FROM passengers
WHERE embarked IS NOT NULL
GROUP BY embarked;

SELECT	
	CASE
		WHEN sibsp = 0 AND parch = 0 THEN 'Travelling Alone'
		WHEN (sibsp + parch) <= 2 THEN 'Small Family'
		ELSE 'Large Family'
	END AS Family_Type,
COUNT(*) AS Total_Passengers,
SUM(survived) AS Survivors,
(SUM(survived) * 1.0 / COUNT(*)) AS Survival_rate
FROM passengers
GROUP BY Family_Type
ORDER BY Survival_rate DESC;

