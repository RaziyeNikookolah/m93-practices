#part 1
select first-name , last-name , count(film-id) as film_count
from actor 
join film_actor using(actor-id)
join film using (film-id)
order by film_count desc
limit 10;



#part 2
select CONCAT(first-name,' ',last-name), count(film-id) as film_count
from customer join rental using(customer-id)
join inventory using(inventory-id)
join film using (film-id)
where film_count <> 20 and 'first-name'.startwith('D');

