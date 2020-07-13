-- SQL 최적화 원리
-- 실행 계획을 봐야 함
-- ctrl + e 누르기!

select * from emp;

-- #1
select /*+ RULE */ * from emp
 where ROWID = 'AAAHYhAABAAALNJAAN';
 
-- #2 : 인덱스 생성
create index ind_emp on
        emp (ename asc, sal desc);
        
-- #3 : 인덱스 유일 스캔 (Index unique scan)
select *
  from emp
 where empno = 1000;
         
 -- #4 : 인덱스 범위 스캔 (Index Range SCAN)
select empno
  from emp
 where empno >= 1000;
 -- 값이 적어 full scan을 했나봄...
 
 -- #5 : 인덱스 전체 스캔 (Index Full SCAN)
select empno
     , sal
  from emp
 where ename like '%'
   and sal > 0; 
   
-- #6 : 실행계획
select * 
  from emp, dept
 where emp.deptno = dept.deptno
   and emp.deptno = 10;
   
-- #7 : 의도적으로 nested loops 조인 실행
select /*+ ordered use_nl(b) */ *
  from emp a, dept b
 where a.deptno = b.deptno
   and a.deptno = 10;
   
-- #8 : 의도적으로 sort loops 조인 실행
select /*+ ordered use_merge(b) */ *
  from emp a, dept b
 where a.deptno = b.deptno
   and a.deptno = 10;
   
-- #9 : 의도적으로 hash loops 조인 실행
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

