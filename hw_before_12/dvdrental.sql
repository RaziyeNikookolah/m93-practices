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
having film_count between 20 and 25 ;


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

select a1.first_name,a1.last_name
from actor a1 join actor a2
 
on a1.first_name=a2.first_name 
    and a1.last_name=a2.last_name 
    and a1.actor_id <> a2.actor_id


#part 5

select first_name,last_name,sum(amount) as sum_amount
from customer 
join payment using (customer_id)
group by sum_amount
order by sum_amount desc
limit 1;


#part 6

select title from film where title not in (
    select title from film 
    join inventory using(film_id) 
    join rental using (inventory_id);
)


#part 7

select first_name,last_name,length(first_name) as fname_len
from actor 
join film_actor using (actor_id)
where fname_len=8;

#part 8

select title from film 
join inventory using(film_id)
join rental using (inventory_id)
join payment using (rental_id)
join staff using (staff_id)
join store using (store_id)
where store_id=1 and title 
    not in (
    select title from film 
        join inventory using(film_id)
        join rental using (inventory_id)
        join payment using (rental_id)
        join staff using (staff_id)
        join store using (store_id)
        where store_id=2
)

SELECT film_id from inventory
WHERE store_id=1 and film_id not in (SELECT film_id from inventory WHERE store_id=2)

