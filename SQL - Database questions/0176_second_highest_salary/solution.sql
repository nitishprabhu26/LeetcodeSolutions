-- Algorithm:
-- Sort the distinct salary in descend order and then utilize the LIMIT clause to get the second highest salary.

SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1

-- However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there 
-- might be only one record in this table. To overcome this issue, we can take this as a temp table.

------------------------------------------------------------------------

-- Approach 1: Using sub-query and LIMIT clause

SELECT (SELECT DISTINCT salary
        FROM   employee
        ORDER  BY salary DESC
        LIMIT  1 offset 1) AS SecondHighestSalary; 

------------------------------------------------------------------------

-- Approach 2: Using IFNULL and LIMIT clause

SELECT Ifnull((SELECT DISTINCT salary
               FROM   employee
               ORDER  BY salary DESC
               LIMIT  1 offset 1), NULL) AS SecondHighestSalary 

------------------------------------------------------------------------

-- Extra:

Syntax:     IFNULL(expression, alt_value)
-- The IFNULL() function returns a specified value if the expression is NULL.
-- If the expression is NOT NULL, this function returns the expression.

------------------------------------------------------------------------

-- Approach: Using max() function

SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary NOT IN
(SELECT max(Salary) FROM Employee)

------------------------------------------------------------------------