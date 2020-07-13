-- SQL ����ȭ ����
-- ���� ��ȹ�� ���� ��
-- ctrl + e ������!

select * from emp;

-- #1
select /*+ RULE */ * from emp
 where ROWID = 'AAAHYhAABAAALNJAAN';
 
-- #2 : �ε��� ����
create index ind_emp on
        emp (ename asc, sal desc);
        
-- #3 : �ε��� ���� ��ĵ (Index unique scan)
select *
  from emp
 where empno = 1000;
         
 -- #4 : �ε��� ���� ��ĵ (Index Range SCAN)
select empno
  from emp
 where empno >= 1000;
 -- ���� ���� full scan�� �߳���...
 
 -- #5 : �ε��� ��ü ��ĵ (Index Full SCAN)
select empno
     , sal
  from emp
 where ename like '%'
   and sal > 0; 
   
-- #6 : �����ȹ
select * 
  from emp, dept
 where emp.deptno = dept.deptno
   and emp.deptno = 10;
   
-- #7 : �ǵ������� nested loops ���� ����
select /*+ ordered use_nl(b) */ *
  from emp a, dept b
 where a.deptno = b.deptno
   and a.deptno = 10;
   
-- #8 : �ǵ������� sort loops ���� ����
select /*+ ordered use_merge(b) */ *
  from emp a, dept b
 where a.deptno = b.deptno
   and a.deptno = 10;
   
-- #9 : �ǵ������� hash loops ���� ����
select /*+ ordered use_hash(b) */ *
  from emp a, dept b
 where a.deptno = b.deptno
   and a.deptno = 10;

desc emp;
   
select *
from emp
where empno between 1000 and 2000
;

select *
from emp
where (empno >= 1000 and empno <= 2000)
;

select *
from emp
where empno between 2000 and 1000
;

select *
from emp
where (empno >= 2000 and empno <= 1000)
;

select *
from emp
where empno in (1000, 1001)
union all
select *
from emp
where empno in (1000, 1001);



select *
from emp cross join emp
;

select *
from 
(select *
from emp
where empno in (1000, 1001)),
(select '1' as aa
from dual
union 
select '2' as aa
from dual)
;

