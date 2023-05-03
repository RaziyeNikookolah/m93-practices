#part 1
select first-name , last-name , count(film-id) as film_count
from actor 
join film_actor using(actor-id)
join film using (film-id)
group by film_count
order by film_count desc
limit 10;



#part 2
select CONCAT(first-name,' ',last-name), count(film-id) as film_count
from customer join rental using(customer-id)
join inventory using(inventory-id)
join film using (film-id)
where 'first-name'.startwith('D')
group by film_count
having film_count <> 20 ;


#part3
select name ,count(customer-id) as customer_count
from category
join film_category using (category-id)
join film using (film-id)
join inventory using (film-id)
join rental using (inventory-id)
group by customer_count
order by customer_count desc
limit 5 offset 5