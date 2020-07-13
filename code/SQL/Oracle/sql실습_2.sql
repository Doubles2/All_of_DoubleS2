desc plan_table;
-- window function
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between unbounded preceding
                                and unbounded following ) totsal
  from emp;
-- totsal 열에 처음부터 전체의 값이 합해짐

-- window function #2
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between unbounded preceding
                                and current row ) totsal
  from emp;  
-- current row를 이용하면 누적합을 볼 수 있음  

-- window function #3
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between current row
                                and unbounded following ) totsal
  from emp;  
-- 순서를 바꾸면 해당 행에서부터 밑에 값의 총 합을 나타낼 수 있음

-- rank function  
select ename
     , sal
     , job
     , rank() over (order by sal desc) all_rank
     , rank() over (partition by job
                    order by sal desc) job_rank
  from emp;
 --order by job; : 이걸 하면 job_rank의 의미를 파악할 수 있음!
 
-- rank function #2  
select ename
     , sal
     , job
     , rank() over (order by sal desc) all_rank
     , dense_rank() over (partition by job
                    order by sal desc) dense_rank
  from emp
 order by job; --: 이걸 하면 dense_rank의 의미를 파악할 수 있음!  
 
-- rank function #3
select ename
     , sal
     , job
     , rank() over (order by sal desc) all_rank
     , row_number() over (order by sal desc) row_num
  from emp;
 
-- aggregate function
select ename
     , sal
     , mgr
     , sum(sal) over ( partition by mgr) sum_mgr
  from emp;
  
-- 행 순서 관련 function
select deptno
     , ename
     , sal
     , first_value ( ename ) over ( partition by deptno
                                    order by sal desc
                                    rows unbounded preceding) as dept_a
  from emp;
  
-- 행 순서 관련 function #2
select deptno
     , ename
     , sal
     , last_value ( ename ) over ( partition by deptno
                                    order by sal desc
                                    rows between unbounded preceding
                                             and unbounded following) as dept_a
  from emp;                                      

-- 행 순서 관련 function #3
select deptno
     , ename
     , sal
     , lag ( sal ) over ( order by sal desc ) as pre_sal
  from emp;
  
-- 행 순서 관련 function #4
select deptno
     , ename
     , sal
     , lead ( sal, 2 ) over ( order by sal desc ) as pre_sal
  from emp;                                                                                  
  
-- 비율 관련 function
select deptno
     , ename
     , sal
     , percent_rank() over ( partition by deptno
                                 order by sal desc ) as percent_sal
  from emp;                                 
 -- 동일한 값이 있으면 계산은 하되 표시를 바꾸지 않는 군
 
-- 비율 관련 function #2
select deptno
     , ename
     , sal
     , ntile(4) over ( order by sal desc ) as n_tile
  from emp;                                 
 -- sal 기준으로 4분위를 나눠주는 것!