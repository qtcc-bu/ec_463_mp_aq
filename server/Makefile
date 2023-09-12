.PHONY: run
run:
	@sudo docker build -t server .
	@docker run -dp 127.0.0.1:8080:8080 server

.PHONY: clean
clean:
	$(eval PID := $(shell docker ps -q --filter ancestor=server))
	@docker stop $(PID)
	@docker rmi server -f

.PHONY: update
update: clean run
