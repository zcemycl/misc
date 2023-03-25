select distinct(configurations.name), count(deployments.dt)
from configurations
join deployments
on configurations.id = deployments.configuration_id
where year(deployments.dt) = 2021
group by configurations.name
order by count(deployments.dt) desc;
