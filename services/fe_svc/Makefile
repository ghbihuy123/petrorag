DOCKER_REPO := ghbihuy123/petrorag_fe
TIMESTAMP := $(shell date +%Y%m%d_%H%M%S)

up:
	uv run --env-file=.env.dev -m streamlit run app.py --server.address 0.0.0.0

delivery:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_REPO):latest -t $(DOCKER_REPO):$(TIMESTAMP) .
	@echo "Image built successfully!"
	@echo "Tags: latest, $(TIMESTAMP)"
	@echo ""
	@echo "Pushing to DockerHub..."
	docker push $(DOCKER_REPO):latest
	docker push $(DOCKER_REPO):$(TIMESTAMP)
	@echo "Push completed!"