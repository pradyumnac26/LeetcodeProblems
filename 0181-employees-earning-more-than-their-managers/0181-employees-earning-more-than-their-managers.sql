# Write your MySQL query statement below
select e.name as Employee from Employee e join Employee t on e.managerId = t.id where e.salary > t.salary