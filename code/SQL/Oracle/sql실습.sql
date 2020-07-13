-- table ����
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

insert into dept values(10, '�λ���');
insert into dept values(20, '�ѹ���');
insert into dept values(30, 'IT��');

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
   and emp.ename Like '��%'
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

-- ���� ��ȸ
-- max level ���ϱ�
select MAX(level)
  from emp
 start with mgr is NULL
connect by prior empno = mgr;
  
-- node�� data ����
select Level
     , empno
     , mgr
     , ename
  from emp
 start with mgr is null
connect by prior empno = mgr;

-- node�� data ���� : �ð�ȭ ȿ��
select Level
     , lpad(' ', 4 * (LEVEL - 1) ) || empno
     , mgr
     , connect_by_isleaf
  from emp
 start with mgr is null
connect by prior empno = mgr;

-- subquery �����ϱ�
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
  
-- �����༭������ : in
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
        
-- �����༭������ : all
select *
  from emp
 where deptno <= ALL(20, 30);     
 
-- �����༭������ : exists
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
              
-- �����༭������ : scala subquery
select ename "�̸�"
     , sal "�޿�"
     , (
            select avg(sal)
              from emp
        ) "��ձ޿�"
  from emp
 where empno = 1000;
 
 -- �����༭������ : correlated subquery -> main query���� �÷��� subquery���� ����ϴ� ��
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
select decode(deptno, null, '��ü�հ�', deptno)
     , sum(sal)
  from emp
 group by rollup(deptno);

-- rollup #2
select deptno
     , decode(job, null, '�հ�', job)
     , sum(sal)
  from emp
 group by rollup(deptno, job);                 
 
-- grouping function #1
-- return 1 : ��갡�� / return 0 : ���Ұ���
select deptno
     , grouping(deptno)
     , job
     , grouping(job)
     , sum(sal)
  from emp
 group by rollup(deptno, job);

-- grouping function #2
select deptno
     , decode(grouping(deptno), 1, '��ü�հ�') TOT
     , job
     , decode(grouping(job), 1, '�μ��հ�') T_DEPT
     , sum(sal)
  from emp
 group by rollup(deptno, job);

-- grouing sets function
-- �÷��� ������ ������� �پ��� �Ұ踦 ���� �� ����
-- �÷��� ������ ������� ���������� ��� ó����
select deptno
     , job
     , sum(sal)
  from emp
 group by grouping sets(deptno, job);
 
-- cube function
-- ���հ����� ��� ���踦 �����
-- ������ ���� ���� : ��, ������ �� �ִ� ��� ����� ���� ��ȸ
select deptno
     , job
     , sum(sal)
  from emp
 group by cube(deptno, job);
 
 commit