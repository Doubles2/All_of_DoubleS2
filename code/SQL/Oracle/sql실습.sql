-- table 생성
drop table emp;
drop table dept;

create table emp(
  empno  number(10) primary key,
  ename  varchar2(20),
  deptno number(10),
  mgr    number (10),
  job    varchar2(20),
  sal    number(10)
);

insert into emp values(1000, 'test1', 20, NULL, 'CLERK', 800);
insert into emp values(1001, 'test2', 30, 1000, 'SALESMAN', 1600);
insert into emp values(1002, 'test3', 30, 1000, 'SALESMAN', 1250);
insert into emp values(1003, 'test4', 20, 1000, 'MANAGER', 2975);
insert into emp values(1004, 'test5', 30, 1000, 'SALESMAN', 1250);
insert into emp values(1005, 'test6', 30, 1001, 'MANAGER', 2850);
insert into emp values(1006, 'test7', 10, 1001, 'MANAGER', 2450);
insert into emp values(1007, 'test8', 20, 1006, 'ANALYST', 3000);
insert into emp values(1008, 'test9', 30, 1006, 'PRESIDENT', 5000);
insert into emp values(1009, 'test10', 30, 1002, 'SALESMAN', 1500);
insert into emp values(1010, 'test11', 20, 1002, 'CLERK', 1100);
insert into emp values(1011, 'test12', 30, 1001, 'CLERK', 950);
insert into emp values(1012, 'test13', 20, 1000, 'ANALYST', 3000);
insert into emp values(1013, 'test14', 10, 1000, 'CLERK', 1300);

create table dept (
    deptno number(10),
    dept varchar2(20)
);

insert into dept values(10, '인사팀');
insert into dept values(20, '총무팀');
insert into dept values(30, 'IT팀');

select * from emp;
select * from dept;

-- join
-- equi join
select *
  from emp
     , dept
 where emp.deptno = dept.deptno;

-- inner join
select *
  from emp
  inner join dept
  on emp.deptno = dept.deptno;

-- inner join #2
select *
  from emp
     , dept
 where emp.deptno = dept.deptno
   and emp.ename Like '임%'
 order by ename;

-- intersect
select deptno
  from emp
   intersect
select deptno
  from dept;

-- outer join
select *
  from dept
     , emp
 where emp.deptno (+)= dept.deptno;
 
-- left outer join
select *
  from dept
  left outer join emp
  on emp.deptno = dept.deptno;

-- right outer join
select *
  from dept
  right outer join emp
  on emp.deptno = dept.deptno;
  
-- cross join
select *
  from emp
  cross join dept;
    
-- union / all
select deptno
  from emp
   union all
select deptno
  from emp;  
  -- union : 3 / all : 28
  
-- minus
select deptno
  from dept
   minus
select deptno
  from emp;   

-- 계층 조회
-- max level 구하기
select MAX(level)
  from emp
 start with mgr is NULL
connect by prior empno = mgr;
  
-- node별 data 보기
select Level
     , empno
     , mgr
     , ename
  from emp
 start with mgr is null
connect by prior empno = mgr;

-- node별 data 보기 : 시각화 효과
select Level
     , lpad(' ', 4 * (LEVEL - 1) ) || empno
     , mgr
     , connect_by_isleaf
  from emp
 start with mgr is null
connect by prior empno = mgr;

-- subquery 연습하기
-- subquery
select *
  from emp
 where deptno = 
        (
            select deptno
              from dept
             where deptno = 10
        );
        
-- inline view
select *
  from  (
            select ROWNUM num
                 , ename
              from emp
        ) a
  where num < 5;
  
-- 다중행서브쿼리 : in
select ename
     , job
     , sal
  from emp
     , dept
 where emp.deptno = dept.deptno
   and emp.empno
    in (
            select empno
              from emp
             where sal > 2000
        );
        
-- 다중행서브쿼리 : all
select *
  from emp
 where deptno <= ALL(20, 30);     
 
-- 다중행서브쿼리 : exists
select ename
     , job
     , sal
  from emp
     , dept
 where emp.deptno = dept.deptno
   and exists (
                    select 1
                      from emp
                     where sal > 2000
              );
              
-- 다중행서브쿼리 : scala subquery
select ename "이름"
     , sal "급여"
     , (
            select avg(sal)
              from emp
        ) "평균급여"
  from emp
 where empno = 1000;
 
 -- 다중행서브쿼리 : correlated subquery -> main query내의 컬럼을 subquery에서 사용하는 것
 select empno
      , ename
      , deptno
      , mgr
      , job
      , sal
   from emp a
  where a.deptno = 
                    (
                        select deptno
                          from dept b
                         where b.deptno = a.deptno
                    );
                    
-- group function
-- rollup #1
select decode(deptno, null, '전체합계', deptno)
     , sum(sal)
  from emp
 group by rollup(deptno);

-- rollup #2
select deptno
     , decode(job, null, '합계', job)
     , sum(sal)
  from emp
 group by rollup(deptno, job);                 
 
-- grouping function #1
-- return 1 : 계산가능 / return 0 : 계산불가능
select deptno
     , grouping(deptno)
     , job
     , grouping(job)
     , sum(sal)
  from emp
 group by rollup(deptno, job);

-- grouping function #2
select deptno
     , decode(grouping(deptno), 1, '전체합계') TOT
     , job
     , decode(grouping(job), 1, '부서합계') T_DEPT
     , sum(sal)
  from emp
 group by rollup(deptno, job);

-- grouing sets function
-- 컬럼의 순서와 관계없이 다양한 소계를 만들 수 있음
-- 컬럼의 순서와 관계없이 개별적으로 모두 처리함
select deptno
     , job
     , sum(sal)
  from emp
 group by grouping sets(deptno, job);
 
-- cube function
-- 결합간으한 모든 집계를 계산함
-- 다차원 집계 제공 : 즉, 조합할 수 있는 모든 경우의 수를 조회
select deptno
     , job
     , sum(sal)
  from emp
 group by cube(deptno, job);
 
 commit