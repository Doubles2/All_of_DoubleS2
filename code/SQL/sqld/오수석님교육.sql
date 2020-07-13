# 상황 : 주기적인 데이터 늘리기
select *
  from 
		(select *
           from emp
          where empno in (1000, 1001)),
(select '1' as aa
   from dual
  union 
 select '2' as aa
   from dual);