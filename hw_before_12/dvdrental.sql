#part 1
select first_name , last_name , count(film_id) as film_count
from actor 
join film_actor using(actor_id)
join film using (film_id)
group by film_count
order by film_count desc
limit 10;



#part 2
select CONCAT(first_name,' ',last_name), count(film_id) as film_count
from customer join rental using(customer_id)
join inventory using(inventory_id)
join film using (film_id)
where first_name.startwith('D')
group by film_count
having film_count <> 20 ;


#part3
select name ,count(customer_id) as customer_count
from category
join film_category using (category_id)
join film using (film_id)
join inventory using (film_id)
join rental using (inventory_id)
group by customer_count
order by customer_count desc
limit 5 offset 5


#part 4

select first_name,last_name,actor_id
from actor join film_actor using(actor_id)
where first_name=last_name


#part 5

select first_name,last_name,sum(amount) as sum_amount
from customer 
join payment using (customer_id)
group by sum_amount
order by sum_amount desc
limit 1;


#part 6


