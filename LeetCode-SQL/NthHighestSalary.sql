CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE N_val INT;
SET N_val = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT(salary)
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N_val
  );
END