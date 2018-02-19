# Task 1: Docker, RabbitMQ

### Step 1 (start consumer, RabbitMQ and MongoDB)

	docker-compose up --build
	
### Step 2 (build producer)

	docker build ./producer -t producer

### Step 3 (start producer)

	docker run -it --rm --network=1_default producer