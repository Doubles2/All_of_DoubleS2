desc plan_table;
-- window function
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between unbounded preceding
                                and unbounded following ) totsal
  from emp;
-- totsal ���� ó������ ��ü�� ���� ������

-- window function #2
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between unbounded preceding
                                and current row ) totsal
  from emp;  
-- current row�� �̿��ϸ� �������� �� �� ����  

-- window function #3
select empno
     , ename
     , sal
     , sum(sal) over (order by sal
                        rows between current row
                                and unbounded following ) totsal
  from emp;  
-- ������ �ٲٸ� �ش� �࿡������ �ؿ� ���� �� ���� ��Ÿ�� �� ����

-- rank function  
select ename
     , sal
     , job
     , rank() over (order by sal desc) all_rank
     , rank() over (partition by job
                    order by sal desc) job_rank
  from emp;
 --order by job; : �̰� �ϸ� job_rank�� �ǹ̸� �ľ��� �� ����!
 
-- rank function #2  
select ename
     , sal
     , job
     , rank() over (order by sal desc) all_rank
     , dense_rank() over (partition by job
                    order by sal desc) dense_rank
  from emp
 order by job; --: �̰� �ϸ� dense_rank�� �ǹ̸� �ľ��� �� ����!  
 
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
  
-- �� ���� ���� function
select deptno
     , ename
     , sal
     , first_value ( ename ) over ( partition by deptno
                                    order by sal desc
                                    rows unbounded preceding) as dept_a
  from emp;
  
-- �� ���� ���� function #2
select deptno
     , ename
     , sal
     , last_value ( ename ) over ( partition by deptno
                                    order by sal desc
                                    rows between unbounded preceding
                                             and unbounded following) as dept_a
  from emp;                                      

-- �� ���� ���� function #3
select deptno
     , ename
     , sal
     , lag ( sal ) over ( order by sal desc ) as pre_sal
  from emp;
  
-- �� ���� ���� function #4
select deptno
     , ename
     , sal
     , lead ( sal, 2 ) over ( order by sal desc ) as pre_sal
  from emp;                                                                                  
  
-- ���� ���� function
select deptno
     , ename
     , sal
     , percent_rank() over ( partition by deptno
                                 order by sal desc ) as percent_sal
  from emp;                                 
 -- ������ ���� ������ ����� �ϵ� ǥ�ø� �ٲ��� �ʴ� ��
 
-- ���� ���� function #2
select deptno
     , ename
     , sal
     , ntile(4) over ( order by sal desc ) as n_tile
  from emp;                                 
 -- sal �������� 4������ �����ִ� ��!