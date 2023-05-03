select first-name , last-name , count(film-id) as film_count
from actor 
join film_actor using(actor-id)
join film using (film-id)
order by film_count desc
limit 10
