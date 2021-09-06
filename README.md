# apartment-cron-manager

## purpose

lambda function that turns ecs services on and off programmatically. 

## interface

json format with the following structure and expected data types:

```
{"service": (str), "status":(str)}
```

### supported services
- "apartment-app-server"
- "di-vita"

### supported statuses
- "1"
- "0"