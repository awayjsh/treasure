-- 01. Querying data

SELECT LastName FROM employees;
SELECT LastName,FirstName FROM employees;
SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;

-- 02. Sorting data

SELECT FirstName FROM employees ORDER BY FirstName DESC;

SELECT Country, City From customers ORDER BY Country DESC, City ASC; 

SELECT
    Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
    tracks
ORDER BY
    Milliseconds DESC;

-- NULL 정렬 예시

SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;

-- 03. Filtering data

SELECT DISTINCT
    Country
FROM
    customers
ORDER BY
    Country;

-- 04. Grouping data

SELECT
    LastName, FirstName, City
FROM
    customers
WHERE
    City = 'Prague';


-- 에러


-- 에러 해결
