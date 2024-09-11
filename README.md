# API Documentation

## POST /register

Creates a new user:

Accepts a user object:
```json
{
    "user": {
    "id": 3,
    "location": "Nairobi",
    "name": "Fickie Long",
    "username": "fickie"
    }
}
```

Returns the user object if created successfully

## POST /login

Logs a user into an existing account

Accepts a user object with username and password:
```json
{
    "user": {
        "username": "fickie",
        "password": "Fickie@1824"
    }
}
```

Returns the user object and a JWT token:
```json
{
	"user": {
		"id": 3,
        "location": "Nairobi",
        "name": "Fickie Long",
        "username": "fickie"
	},
	"jwt": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNn0.TeQZt3vwCQpLhBV0VkqOM2T4Q1VLvQFU7NYwzwbZ8Hc"
}
```

### GET /me

Returns the user object if authenticated by a bearer token:
```json
{
	"user": {
		"id": 3,
        "location": "Nairobi",
        "name": "Fickie Long",
        "username": "fickie"
	}
}
```

If not authenticated, returns a message:

```json
{
	"message": "Please log in"
}
```

### POST /auto_login

Takes in a JWT:

```json
{
    "jwt": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNn0.TeQZt3vwCQpLhBV0VkqOM2T4Q1VLvQFU7NYwzwbZ8Hc"
    
}
```

Returns the user object matching that token:

```json
{
	""id": 3,
    "location": "Nairobi",
    "name": "Fickie Long",
    "username": "fickie"
}
```

## GET /active_days

Returns a list of active days and the user they belong to:

```json
[
	{
		"id": 1,
		"date": "2024-08-31",
		"day_of_week": "wednesday",
		"streak": 4,
		"user_id": 1
	},
	{
		"id": 2,
		"date": "2022-08-30",
		"day_of_week": "tuesday",
		"streak": 3,
		"user_id": 1
	}
]
```

## GET /active_days/:id

Returns a single active days found by id:

```json
{
	"active_day": {
		"id": 1,
		"date": "2022-08-31",
		"day_of_week": "wednesday",
		"streak": 4,
		"user_id": 1
	}
}
```

## POST /active_days

Accepts an active_day JSON object with keys date, day_of_week, streak, and user_id:

```json
{
	"active_day": {
		"date": "2022-08-31",
		"day_of_week": "wednesday",
		"streak": 4,
		"user_id": 1
	}
}
```
Returns the JSON object with its newly created id:

```json
{
	"active_day": {
		"id": 8,
		"date": "2022-08-31",
		"day_of_week": "wednesday",
		"streak": 4,
		"user_id": 1
	}
}
```

## DELETE /active_days/:id

Destroys the ActiveDay record associated with the provided ID

## GET /activities

Returns a list of activities and the user they belong to:

```json
[
	{
		"id": 1,
		"active_day_id": 1,
		"exercise_type": "bike",
		"activity_length": 93,
		"calories": 1063,
		"distance": 12.65,
		"streak": 3,
		"rating": 8,
		"summary": "good"
	},
	{
		"id": 2,
		"active_day_id": 1,
		"exercise_type": "run",
		"activity_length": 73,
		"calories": 1163,
		"distance": 7.01,
		"streak": 1,
		"rating": 9,
		"summary": "good"
	},
	{
		"id": 3,
		"active_day_id": 2,
		"exercise_type": "bike",
		"activity_length": 49,
		"calories": 560,
		"distance": 8.69,
		"streak": 2,
		"rating": 7,
		"summary": "good"
	}
]
```

## GET /activities/:id

Returns a single activity found by id:

```json
{
	"activity": {
		"id": 1,
		"active_day_id": 1,
		"exercise_type": "bike",
		"activity_length": 93,
		"calories": 1063,
		"distance": 12.65,
		"streak": 3,
		"rating": 8,
		"summary": "good"
	}
}
```

## POST /activities

Accepts an activity JSON object with keys active_day_id, exercise_type, activity_length, calories, distance, streak, rating, and summary:

```json
{
	"activity": {
		"active_day_id": 3,
		"exercise_type": "run",
		"activity_length": 43,
		"calories": 603,
		"distance": 4.23,
		"streak": 3,
		"rating": 6,
		"summary": "ok"
	}
}
```
Returns the JSON object with its newly created id:

```json
{
	"activity": {
		"id": 12,
		"active_day_id": 3,
		"exercise_type": "run",
		"activity_length": 43,
		"calories": 603,
		"distance": 4.23,
		"streak": 3,
		"rating": 6,
		"summary": "ok"
	}
}
```

## DELETE /activities/:id

Destroys the Activity record associated with the provided ID

## GET /active_days/:id/activities

Returns the activities associated with the id of a particular active_day:

```json
[
	{
		"id": 1,
		"active_day_id": 1,
		"exercise_type": "bike",
		"activity_length": 93,
		"calories": 1063,
		"distance": 12.65,
		"streak": 3,
		"rating": 8,
		"summary": "good"
	},
	{
		"id": 2,
		"active_day_id": 1,
		"exercise_type": "run",
		"activity_length": 73,
		"calories": 1163,
		"distance": 7.01,
		"streak": 1,
		"rating": 9,
		"summary": "good"
	}
]
```

## GET /activities/:exercise_type/top/:column

Takes 2 params in the request, returns the record with the highest attribute in the column specified, for the activity specified

Example URI - "http://localhost:3000/activities/bike/top/calories" will return "exercise_type: bike" records ordered by the highest value in the calories column, along with their associated active_day records

```json
[
	{
		"id": 15,
		"active_day_id": 12,
		"exercise_type": "bike",
		"activity_length": 45,
		"calories": 54,
		"distance": 45.0,
		"streak": null,
		"rating": 5,
		"summary": null,
		"created_at": "2022-09-14T16:50:23.473Z",
		"updated_at": "2022-09-14T16:50:23.473Z",
		"active_day": {
			"id": 12,
			"date": "2022-09-15",
			"day_of_week": "Thursday",
			"streak": 2,
			"user_id": 2,
			"created_at": "2022-09-14T16:50:23.399Z",
			"updated_at": "2022-09-14T16:50:23.399Z"
		}
	},
	{
		"id": 4,
		"active_day_id": 3,
		"exercise_type": "bike",
		"activity_length": 121,
		"calories": 1383,
		"distance": 18.25,
		"streak": 1,
		"rating": 6,
		"summary": "good",
		"created_at": "2022-09-13T18:18:36.523Z",
		"updated_at": "2022-09-13T18:18:36.523Z",
		"active_day": {
			"id": 3,
			"date": "2022-08-29",
			"day_of_week": "monday",
			"streak": 2,
			"user_id": 1,
			"created_at": "2022-09-13T18:18:36.466Z",
			"updated_at": "2022-09-13T18:18:36.466Z"
		}
	}
]
```